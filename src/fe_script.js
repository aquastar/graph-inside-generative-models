  
    // The Für Elise chain beside interest 3 plays in two acts. First it learns:
    // the ball walks the melody and every move it makes draws (or thickens) an
    // arrow. Then it composes: each note shows a spinner whose wedges are its
    // outgoing probabilities, and the needle picks where the ball goes next.
    const chain = document.querySelector('.fe-chain');
    if (chain) {
      const notes = JSON.parse(document.querySelector('.fe-notes').textContent);
      const melody = JSON.parse(chain.dataset.melody);
      const durations = JSON.parse(chain.dataset.durations);
      const wedges = JSON.parse(chain.dataset.wedges);
      const heldFor = new Map();
      melody.forEach((n, i) => heldFor.set(n, [...(heldFor.get(n) ?? []), durations[i]]));
      const ball = chain.querySelector('.fe-ball');
      const status = chain.querySelector('.fe-status');
      const nodeEl = (n) => chain.querySelector(`[data-note="${n}"]`);
      const edgeEl = (a, b) => chain.querySelector(`[data-edge="${a}>${b}"]`);
      let run = 0;
      const sleep = (ms) => {
        const tk = run;
        return new Promise((r) => setTimeout(() => { if (tk === run) r(); }, ms));
      };

      if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
        chain.querySelectorAll('.fe-edge').forEach((e) => e.classList.add('is-on'));
        chain.classList.add('is-composing');
        status.textContent = 'learned from Für Elise';
      } else {
        // Hold still while the figure is off screen or the tab is hidden.
        let visible = (window.parent === window);
        window.addEventListener('message', (e) => { if (e.data === 'fe-play') { visible = true; run += 1; play(); } if (e.data === 'fe-stop') { visible = false; run += 1; audio?.suspend(); } });
        const waitVisible = () => new Promise((r) => {
          const tk = run;
          const check = () => {
            if (tk !== run) return;
            if (visible) r(); else setTimeout(check, 300);
          };
          check();
        });

        // Sound only plays inside the dialog, which the viewer opened by clicking.
        let audio = null;
        const sound = (n) => {
          if (!audio) return;
          const t = audio.currentTime;
          const osc = audio.createOscillator();
          const gain = audio.createGain();
          osc.type = 'triangle';
          osc.frequency.value = 440 * 2 ** ((60 + notes[n][3] - 69) / 12);
          gain.gain.setValueAtTime(0.0001, t);
          gain.gain.exponentialRampToValueAtTime(0.22, t + 0.01);
          gain.gain.exponentialRampToValueAtTime(0.0001, t + 0.45);
          osc.connect(gain).connect(audio.destination);
          osc.start(t);
          osc.stop(t + 0.5);
        };
        // The staff keeps the last fifteen notes, the newest on the right. Each
        // new note arrives by a red arc hopping from the note before it.
        const score = chain.querySelector('.fe-score');
        const SVGNS = 'http://www.w3.org/2000/svg';
        const svgEl = (tag, attrs) => {
          const el = document.createElementNS(SVGNS, tag);
          Object.entries(attrs).forEach(([k, v]) => el.setAttribute(k, v));
          return el;
        };
        const SLOT = 18;
        const staffStep = (n) => (Number(n.at(-1)) - 4) * 7 + 'CDEFGAB'.indexOf(n[0]) - 2;
        let lastY = null;
        const write = (n) => {
          const step = staffStep(n);
          const y = 132 - step * 2;
          const color = notes[n][2];
          const g = svgEl('g', {});
          const mark = svgEl('g', {});
          if (step <= -2) mark.append(svgEl('line', { x1: -5, y1: 136, x2: 5, y2: 136, stroke: '#94a3b8', 'stroke-width': .6 }));
          if (n.includes('#')) {
            const sharp = svgEl('text', { x: -8, y: y + 2.5, 'font-size': 7, fill: color });
            sharp.textContent = '♯';
            mark.append(sharp);
          }
          mark.append(svgEl('ellipse', { cx: 0, cy: y, rx: 2.9, ry: 2.1, fill: color, transform: `rotate(-20 0 ${y})` }));
          mark.append(step >= 4
            ? svgEl('line', { x1: -2.6, y1: y + 1, x2: -2.6, y2: y + 11, stroke: color, 'stroke-width': .8 })
            : svgEl('line', { x1: 2.6, y1: y - 1, x2: 2.6, y2: y - 11, stroke: color, 'stroke-width': .8 }));
          g.append(mark);
          let arc = null;
          let dot = null;
          if (lastY !== null) {
            arc = svgEl('path', { d: `M${-SLOT} ${lastY - 3} Q${-SLOT / 2} ${Math.min(lastY, y) - 14} 0 ${y - 3}`, fill: 'none', stroke: '#dc2626', 'stroke-width': .8, opacity: .75 });
            dot = svgEl('circle', { r: 1.9, cx: -SLOT, cy: lastY - 3, fill: '#dc2626' });
            g.prepend(arc);
            g.append(dot);
            mark.style.opacity = 0;
          }
          lastY = y;
          score.append(g);
          while (score.children.length > 15) score.firstChild.remove();
          [...score.children].forEach((c, k, all) => c.setAttribute('transform', `translate(${286 - (all.length - 1 - k) * SLOT} 0)`));
          const len = arc ? arc.getTotalLength() : 0;
          if (arc) { arc.style.strokeDasharray = len; arc.style.strokeDashoffset = len; }
          return {
            move(f) {
              if (!arc) return;
              arc.style.strokeDashoffset = len * (1 - f);
              const pt = arc.getPointAtLength(f * len);
              dot.setAttribute('cx', pt.x);
              dot.setAttribute('cy', pt.y);
            },
            done() { mark.style.opacity = ''; dot?.remove(); },
          };
        };
        const land = (n) => {
          ball.setAttribute('cx', notes[n][0]);
          ball.setAttribute('cy', notes[n][1]);
          chain.querySelectorAll('.fe-node.is-now').forEach((e) => e.classList.remove('is-now'));
          nodeEl(n).classList.add('is-now');
          sound(n);
        };
        // Transition probability shown beside the edge in play. While learning
        // it is the share counted so far, so the fractions settle as it reads.
        const prob = chain.querySelector('.fe-prob');
        const seen = new Map();
        const fraction = (k, total) => (k === total ? '100%' : `${k}/${total}`);
        const label = (path, text) => {
          const pt = path.getPointAtLength(path.getTotalLength() / 2);
          prob.setAttribute('x', pt.x);
          prob.setAttribute('y', pt.y - 3);
          prob.textContent = text;
        };
        const hop = (a, b, ms, text) => new Promise((done) => {
          const path = edgeEl(a, b);
          path.classList.add('is-on', 'is-hot');
          label(path, text);
          const staffMark = write(b);
          const length = path.getTotalLength();
          const t0 = performance.now();
          const tk = run;
          const step = (t) => {
            if (tk !== run) return;
            const f = Math.min(1, (t - t0) / ms);
            const eased = f < 0.5 ? 2 * f * f : 1 - (-2 * f + 2) ** 2 / 2;
            const pt = path.getPointAtLength(eased * length);
            ball.setAttribute('cx', pt.x);
            ball.setAttribute('cy', pt.y);
            staffMark.move(eased);
            if (f < 1) { requestAnimationFrame(step); return; }
            staffMark.done();
            path.classList.remove('is-hot');
            prob.textContent = '';
            land(b);
            done();
          };
          requestAnimationFrame(step);
        });
        // A uniform landing angle picks each wedge with its own probability.
        const spin = async (n, ms = 300) => {
          const angle = Math.random() * 360;
          const ws = wedges[n];
          const pick = ws.find(([, from, span]) => angle >= from && angle < from + span) ?? ws[ws.length - 1];
          const needle = nodeEl(n).querySelector('.fe-needle');
          const turned = Number(needle.dataset.turned ?? 0) + 360;
          needle.dataset.turned = turned;
          needle.style.transition = `transform ${ms}ms cubic-bezier(.2,.7,.2,1)`;
          needle.style.transform = `rotate(${turned + angle}deg)`;
          await sleep(ms + 20);
          return [pick[0], fraction(pick[3], pick[4])];
        };
        const reset = () => {
          chain.querySelectorAll('.fe-edge').forEach((e) => e.classList.remove('is-on', 'is-hot'));
          chain.querySelectorAll('.fe-needle').forEach((nd) => {
            nd.style.transition = 'none';
            nd.style.transform = '';
            nd.dataset.turned = 0;
          });
          chain.classList.remove('is-composing');
          score.replaceChildren();
          lastY = null;
          seen.clear();
          prob.textContent = '';
          chain.querySelector('.fe-composer').textContent = 'composer: Beethoven';
        };

        // Clicking opens the same live figure in a dialog, with sound, and
        // restarts it so the listener hears Für Elise from its first note.
        document.body.addEventListener('click', () => {
          audio ??= new (window.AudioContext || window.webkitAudioContext)();
          audio.resume();
          document.querySelector('.fe-hint').textContent = 'sound on';
          run += 1;
          play();
        });

        const play = async () => {
          for (;;) {
            await waitVisible();
            reset();
            status.textContent = 'learning: every move draws an arrow';
            land(melody[0]);
            write(melody[0]).done();
            // One sixteenth is 170 ms. A longer note holds, then the ball moves.
            const U = 130;
            for (let i = 0; i < melody.length; i += 1) {
              await waitVisible();
              const [a, b] = [melody[i], melody[(i + 1) % melody.length]];
              seen.set(`${a}>${b}`, (seen.get(`${a}>${b}`) ?? 0) + 1);
              const fromA = [...seen].filter(([k]) => k.startsWith(`${a}>`)).reduce((t, [, c]) => t + c, 0);
              await sleep((durations[i] - 1) * U);
              await hop(a, b, U - 20, fraction(seen.get(`${a}>${b}`), fromA));
              await sleep(20);
            }
            await sleep(700);
            chain.classList.add('is-composing');
            status.textContent = 'composing: a spinner at every note';
            chain.querySelector('.fe-composer').textContent = 'composer: the Markov chain';
            score.replaceChildren();
            lastY = null;
            await sleep(700);
            // Composing keeps the tune moving: a quick spin and hop, then the new
            // note holds for a length Beethoven gave that same note somewhere.
            let now = melody[0];
            write(now).done();
            for (let i = 0; i < 24; i += 1) {
              await waitVisible();
              const [next, text] = await spin(now, 120);
              await hop(now, next, 100, text);
              const held = heldFor.get(next) ?? [1];
              await sleep(Math.max(0, held[Math.floor(Math.random() * held.length)] * 190 - 240));
              now = next;
            }
            status.textContent = 'a tune Beethoven never wrote';
            await sleep(2600);
          }
        };
        play();
      }
    }
  
