## 调研报告：音乐研究中的图，哪些有用，哪些没用（面向 CS 系内 45 分钟报告）

说明：所有引文均经网页抓取核实，除非在 H 节标注。部分页面被工具权限拦截，无法打开，也在 H 节列出。全文不含破折号和分号。

---

## A. 总表

| 工作或研究线 | 节点 / 边 | 任务 | 比非图方法好吗，或揭示了别的方法看不到的东西 | 有用程度 | 来源（已核实） |
|---|---|---|---|---|---|
| Hiller and Isaacson 1957, Illiac Suite 第四乐章 | 节点 = 音高或音程状态，边 = 转移概率（Markov chain） | 计算机作曲 | 第一个用随机过程写出可演奏乐曲，没有 baseline 概念，只是证明可行 | 有用（历史起点，可听） | Wikipedia Illiac Suite 页，OpenCulture 2019 文章，Experimental Music (McGraw-Hill 1959) |
| Conklin and Witten 1995, multiple viewpoint systems | 节点 = 事件（音高、时值、音程等多个 viewpoint 各自一条链），边 = 变阶 n-gram 转移 | 旋律预测（Bach chorales 的交叉熵） | 多视角组合比单一链预测熵更低，证明"几条小图合起来"比"一张大图"好 | 有用 | JNMR 24(1):51 to 73, 1995 |
| Pachet 2003, Continuator | 节点 = 乐句前缀（prefix tree），边 = 变阶 Markov 延续 | 实时即兴对话 | 没有量化 baseline，但儿童研究（Addessi and Pachet 2005）显示孩子能认出自己的风格被模仿 | 有用（交互示范），证据偏定性 | JNMR 32(3):333 to 341, 2003 |
| Pachet and Roy 2011, Markov constraints | 同上链，外加约束满足把 Markov 概率写成 elementary Markov constraints | 可控生成（和弦序列、风格旋律） | 比贪心左到右采样多付计算，换来任意约束下的可控性 | 有用（告诉听众"图上加约束 = 可控") | Constraints 16(2):148 to 172, 2011 |
| Papadopoulos, Roy, Pachet 2014, MaxOrder | 把语料编译成自动机（节点 = 状态，边 = 允许的转移），禁止超过 max order 的语料片段 | 避免 Markov 生成抄袭 | 揭示了一个别的方法看不到的问题：高阶链会整段复制语料，阶数限制的是上下文长度而不是复制长度。线性时间构造自动机 | 有用（直接对应"去风格不加风格"的抄袭/记忆问题） | AAAI 2014 |
| Pearce 2005 / 2018, IDyOM | 多视角变阶 Markov（PPM），短期 + 长期模型，输出每个音的 information content 和 entropy | 旋律期待建模，认知预测 | 预测人类期待评分和脑响应（见 Di Liberto 2020）。它是"图"而且是能对接大脑的图 | 非常有用 | Pearce 2005 PhD thesis, City University London。Pearce 2018 Ann NY Acad Sci, doi 10.1111/nyas.13654。github.com/mtpearce/idyom |
| Tonnetz 及其轨迹（Karystinaios, Guichaoua, Andreatta, Bigo, Bloch 2020；Bergomi et al. 拓扑指纹） | 节点 = 12 个音级，边 = 五度和三度，三角形 = 三和弦。乐曲在其上走的轨迹再转成加权图，算中心性和聚类系数 | 体裁/作曲家分类 | 8 类作曲家：只用轨迹描述子 F1 0.49，只用 MIDI 元信息 0.76，合并 0.82。4 大风格组：轨迹 0.84，全部 0.94。轨迹单独并不强，但有补充信息 | 有限（好看，可解释，但单独不如朴素特征） | JIM 2020 preprint，arXiv 1602.00739 |
| 音符转移复杂网络（Liu, Tse, Small 2010；Ferretti 2016/2017 吉他 solo） | 节点 = 音符（Ferretti 还带八度和时值），边 = 相邻或共现，权重 = 次数 | 描述统计（幂律度分布、小世界），随机游走生成 | Liu et al. 报告幂律和"保持这些性质是作曲必要条件"的猜想，生成结果只有主观好听评价。Ferretti 只做描述，无分类器，无非图 baseline，单曲是否小世界结果不一 | 不太有用（描述性，无对照） | Physica A 389(1):126 to 132, 2010。arXiv 1610.00468 |
| 和弦网络（Buongiorno Nardelli 2020；Moss et al. 2019 贝多芬四重奏） | 节点 = 和弦，边 = 相继进行 | 调性区域切分，和声统计 | Moss et al.：和弦频率近似幂律，转移有方向性，不是网络论文。Buongiorno Nardelli 声称调性的中心性和层级"从拓扑涌现"，无对照 | 有限 | arXiv 2006.01033。PLoS One 14(6) e0217242, 2019 |
| 作曲家网络（Park, Bae, Schich, Park 2015） | 节点 = 作曲家，边 = 同一张 CD 共同出现 | 网络增长机制 | 超线性优先连接，录音集中化。是关于音乐产业的社会网络，不是关于音乐本身 | 有限（与报告主题无关） | EPJ Data Science 4:2, 2015 |
| 乐曲结构图（McFee and Ellis 2014，librosa Laplacian segmentation） | 节点 = 节拍帧，边 = 重复边（和声相似的远距离互为 k 近邻）+ 顺序边（相邻帧） | 曲式分段（verse, chorus） | Laplacian 特征向量分层分段。自动选层只在 F0.5 上全面胜过非图基线 SMGA，oracle 选层在 SALAMI 上全面胜出，Beatles 上 F3 和 Fpair 仍输。但多层级结构是非图方法给不出的 | 有用（MIR 里图真正带来新东西的例子，而且可听） | ISMIR 2014 pp. 405 to 410 |
| 乐谱 GNN：Jeong, Kwon, Kim, Nam 2019 VirtuosoNet | 节点 = 音符，边 = 同时发声、相继、同小节等关系 | 从乐谱生成有表情的钢琴演奏 | 听测中比把乐谱当词序列的层次注意力网络"更像人"。没有客观指标胜出的证据 | 有用（唯一有听测的乐谱 GNN） | ICML 2019, PMLR 97:3060 to 3070 |
| 乐谱 GNN：Karystinaios and Widmer 2022 终止式检测 | 节点 = 音符和休止，边 = 同起音、相继、覆盖 | 节点分类（终止式小于 2% 的节点） | Bach PAC：手工特征 SVM 0.80，GNN 0.73，预训练 GNN 0.80。Haydn PAC：SVM 0.69，GNN 0.59。内部对照：无图卷积 0.667，两跳 0.732。结论：图卷积有帮助，但整体只打平手工特征 | 有限（诚实的例子：图不自动赢） | ISMIR 2022 |
| GraphMuse（Karystinaios and Widmer 2024） | 同上乐谱图，加针对乐谱的邻居采样和层次模块 | 库，pitch spelling 和终止式检测 | 声称显著超过以前方法，页面无数字，未说明对比对象是否非图 | 有限（工程贡献） | ISMIR 2024 |
| 音乐知识图谱推荐（Ostuni, Oramas, Di Noia, Serra, Di Sciascio, ACM TIST 2016/2017） | 节点 = 歌曲、声音、标签、DBpedia 和 WordNet 实体，边 = 语义链接 | 推荐 | 在 Freesound 和 Songfacts+Last.fm 上显著超过协同过滤，并提高多样性和新颖性 | 有用但与"音乐内部有没有图"无关，图在音乐外面 | sisinflab.poliba.it 页面，doi 10.1145/2926718 |
| 用户-歌曲二部图 GNN 推荐（如 Jayakumar and Özoğlu 2025 预印本） | 节点 = 用户、曲目、体裁，边 = 收听或所属 | 推荐 | 预印本声称超过 MFCC 和协同过滤，无数字可核 | 不推荐在报告中用 | arXiv 2504.02598 |
| 生成模型内部的图：注意力可视化（Huang, Dinculescu, Vaswani, Eck 2018） | 节点 = 音符，边 = 自注意力权重 | 解释 Music Transformer | 发现相对注意力在 JSB chorales 上更稳定地关注前一拍所有声部和终止式处的乐句开头，是"从模型里读出的图" | 有用（唯一一个"图在生成模型里面"的直接证据，但是定性的） | NIPS 2018 Interpretability workshop；magenta.github.io/music-transformer-visualization |
| 生成模型内部的图：探针（Castellon, Donahue, Liang 2021；Wei, Freeman, Donahue, Sun 2024） | 不是图，是线性/MLP 探针读中间层 | 看中间层编码了什么 | Castellon：Jukebox 表示比标签预训练表示平均好约 30%，调性检测差距最大。Wei：Jukebox 平均 0.984，MusicGen small 0.950 大于 medium 0.914 和 large 0.929，手工特征合集 0.936，chroma 0.878，EnCodec 码本 0.701，深层更好 | 非常有用（给"图在不在里面"提供方法论） | arXiv 2107.05677（ISMIR 2021，venue 由作者页面确认，arXiv 页不写）。ISMIR 2024 |
| 听音乐时的脑功能网络（Wilkins, Laurienti, Hodges, Steen, Burdette 2014） | 节点 = 体素，边 = fMRI 时间序列相关 | 偏好音乐对连接的影响 | 喜欢的歌改变听觉皮层与海马的连接，默认模式网络连接随偏好而非体裁变化，古典乐听觉皮层内度更高 | 有限（是脑的图，不是音乐的图，对本报告只做背景） | Scientific Reports 4:6130, 2014 |
| 从活动里读出的状态转移图 | 文献检索未找到针对音乐生成模型的此类工作 | | | 这是报告者自己的空位 | 无 |

---

## B. 有用的图（排名）

1. IDyOM（Pearce）。变阶 Markov 就是带概率的转移图。它是唯一一个既预测人类期待又预测脑电（Di Liberto 2020）的音乐图。对报告的意义：报告者的 12 节点链是 IDyOM 的极简版，脑可以当裁判这件事有先例。
2. 乐曲结构图（McFee and Ellis 2014）。远距离重复边是序列模型天然丢掉的信息，Laplacian 分层把 verse 和 chorus 切出来。可听：放一首歌，屏幕上同步显示分段。证据诚实：不是全面胜出，但给出了非图方法没有的多层级结构。
3. MaxOrder 自动机（Papadopoulos, Roy, Pachet 2014）。揭示了"阶数限制上下文，不限制抄袭长度"。对报告的意义：直接呼应"去掉风格容易，加上风格会变成复制"。
4. Conklin and Witten 多视角 + Continuator 变阶链。证明小图的组合比大图好，和实时可交互。Continuator 儿童研究是最好讲的故事：三到五岁的孩子能认出自己的风格被学走了。
5. 探针（Castellon 2021，Wei 2024）。不是图，但它是"模型内部有没有乐理结构"的标准测法。要点：MusicGen small 探针成绩高于 large，手工 chroma 在静态音级任务上和模型打平，只在随时间变化的和弦进行上输。
6. 注意力图（Huang et al. 2018）。从 Music Transformer 里读出来的音符间关系图，在终止式处指回乐句开头。这是"生成模型里有图"的唯一直接可视化，可以当引子，然后说"但它是定性的，我们要定量"。
7. VirtuosoNet（Jeong 2019）。乐谱 GNN 中唯一有听测胜出的，证明"同时发声"这种边是序列丢掉的。
8. 音乐知识图谱推荐（Ostuni et al. 2016/2017）。只在需要说"产业里图在音乐外面"时提一句。

---

## C. 没用或被高估的图

- 音符转移"复杂网络"（Liu, Tse, Small 2010 及后续）。幂律和小世界结论无对照，随机图 baseline 只能证明"不是随机"，没有任何分类或预测任务。Ferretti 的吉他 solo 网络连单曲是否小世界都不一致，并且合并后指标改变。报告中可用一句话点名：度分布漂亮不等于有用。
- Tonnetz 轨迹单独做分类（Karystinaios et al. 2020）。8 类 F1 0.49，比 MIDI 元信息 0.76 低很多。Tonnetz 适合讲解，不适合当证据。
- 作曲家 CD 共现网络（Park et al. 2015）。是社会学，和"音乐里有没有图"无关。
- 用户-歌曲二部图推荐。图里的节点是人和商品，音乐只是 item，结论不转移到音乐内部。
- 和弦网络的"调性从拓扑涌现"（Buongiorno Nardelli 2020）。预印本，无对照，谨慎引用。
- 乐谱 GNN 不该被说成"图赢了"。终止式检测最好情况只打平手工特征 SVM，Haydn 上输。可以反过来用：图上加对的边（同时发声、覆盖）才有增益，加错了没用。

---

## D. 幻灯片建议（替换"four stages of graphs in music"）

**Slide 1. Headline: "The oldest music model is a 12-node graph, and it still works"**
画面：左边 12 个音级节点的有向加权图（报告者自己的 144 个数字），右边 1957 年 Illiac Suite 第四乐章的乐谱片段或 Hiller 的照片。
讲稿：1957 年第一首计算机作曲就是在这种图上随机游走。1995 年 Conklin 和 Witten 证明几条小链组合比一条大链预测得更准。2003 年 Pachet 的 Continuator 用同样的链和三岁小孩对弹，孩子能听出自己的风格被学走。我们做的事只是把这条链压到 144 个数字，然后问它能不能认出一首曲子来自哪个传统：六个语料库上 70.9%。放一段用 144 个数字生成的旋律，再放一段原曲。

**Slide 2. Headline: "A graph on music helps only when its edges carry what the sequence throws away"**
画面：两列。左列 McFee and Ellis 的重复图（节拍为节点，远距离相似为边）和由此切出的 verse/chorus 彩色分段，下面放一段可播放的歌。右列一张小表：终止式检测 SVM 0.80 对 GNN 0.73 到 0.80，Tonnetz 轨迹 0.49 对元信息 0.76。
讲稿：MIR 里真正靠图赢的地方是结构分段，因为"第 40 拍和第 120 拍很像"这条边，序列模型天然看不见。反例也要说：把乐谱做成 GNN 去找终止式，只打平手工特征。音符共现网络的幂律很漂亮，但从来没有拿它完成过任务。结论：图是否有用取决于边是不是编码了序列丢掉的东西，这正是我们要去生成模型里检查的。

**Slide 3. Headline: "Neural generators hide no graph by design, so we read one out and let the brain check it"**
画面：上半部分 MusicGen 的四条 token 流加延迟，旁边一张从中间层读出的转移图。下半部分一条 EEG 曲线，叠上 IDyOM 的 surprise（Di Liberto 2020）和 MusicGen 的 surprisal（Noguchi 2026）。
讲稿：MusicGen 内部没有乐理，只有下一个 token 的概率。探针研究发现乐理概念在中间层可以线性读出，但模型越大反而不一定越清楚。我们换一个读法：读出 12 节点的转移图，然后做两件事，一是操控它看风格能不能加减（只能减不能加），二是把模型的 surprise 和听众脑电对齐。Di Liberto 用 Markov 图的 surprise 解释了听 Bach 时 200 毫秒附近的脑电成分，Noguchi 用 MusicGen 的 surprisal 把脑电识曲准确率从 0.823 提到 0.887。大脑是不依赖任何乐理的裁判。

---

## E. MusicGen 与探针的通俗文本（幻灯片用，英文）

**(a) What MusicGen is (Copet et al., NeurIPS 2023)**
MusicGen never sees a waveform. An audio compressor called EnCodec turns every 20 milliseconds of 32 kHz sound into four small integers, one from each of four codebooks of 2,048 entries, so one second of music is 50 steps of four tokens. A single Transformer then does what GPT does with words: given the tokens so far and a text description encoded by T5, predict the next token. The four codebooks are staggered by one step each (the delay pattern), so all four can be predicted together at 50 steps per second instead of 200, with almost no loss in quality (the paper reports FAD 0.96 for delay versus 0.86 for the four times costlier flattened order). That is the whole model, which is why it is fair to call it a next token predictor for audio, and why anything like a key or a style inside it must be an emergent property, not a design choice.
（中文备注：这段里的数字出自论文 3.1 节和 4.4 节 Table 4，已核实。）

**(b) What probing found**
Castellon, Donahue and Liang (ISMIR 2021) froze Jukebox, a music generator trained on a million songs, read out its middle layers, and trained tiny classifiers on them. Those readouts beat the best representations pre-trained on tags by about 30 percent on average across tagging, genre, emotion and key detection, with the largest gap on key, so a model trained only to continue audio had learned tonality as a side effect. Wei, Freeman, Donahue and Sun (ISMIR 2024) built SynTheory, a synthetic dataset where one music theory concept at a time is varied (tempo, time signature, notes, intervals, scales, chords, chord progressions), and probed Jukebox and three sizes of MusicGen. Headline in one sentence: music theory concepts are linearly readable from the middle to late layers of music generators, Jukebox scores 0.984 on average, but the smallest MusicGen (0.950) beats the medium and large ones, and plain chroma features already tie the models on static tasks like identifying notes, losing only on time varying ones like chord progressions.
（中文备注：数字出自 Wei et al. Table 2，Castellon 的 30% 来自摘要。）

---

## F. 可听材料（已确认存在的 URL）

| 内容 | URL | 页面上有什么 | 核实状态 |
|---|---|---|---|
| MusicGen 样例页 | https://ai.honu.io/papers/musicgen/ | 文生音乐和旋律条件样例（Hugging Face 官方 README 称之为 sample page） | URL 由 facebook/MusicGen Space 的 README 确认，页面本身被权限拦截未打开 |
| MusicGen 在线可玩 | https://huggingface.co/spaces/facebook/MusicGen | Gradio 应用，输入文字现场生成 | Space README 已读取 |
| MusicGen 代码与样例入口 | https://github.com/facebookresearch/audiocraft | NeurIPS 摘要指定的样例、代码、模型位置 | NeurIPS 页面确认，仓库本身未打开 |
| Brain2Music 样例 | https://google-research.github.io/seanet/brain2music | 原刺激与由 fMRI 重建的音乐（检索版和 MusicLM 生成版） | URL 由 arXiv 2307.11078 摘要页确认，页面本身被拦截未打开 |
| Bellier 2023 Pink Floyd 重建音频 | https://doi.org/10.1371/journal.pbio.3002176 | 文章 Supporting information 中 S1 Audio（原曲经幅度谱往返的上界）、S2（线性模型重建，347 个电极）、S3（非线性 MLP 重建）、S4 到 S7（单个病人重建） | 文件清单由 eScholarship 存档的论文 PDF 确认，PLOS 页面本身被拦截 |
| Illiac Suite 第四乐章（Markov chain） | Wikipedia Illiac Suite 条目参考文献中列出四个乐章的 YouTube 链接，第四乐章为 https://www.youtube.com/watch?v=QyqiSbbwHIs | 弦乐四重奏录音 | YouTube 页被拦截，链接只在 Wikipedia 参考文献中见到。另有 Wergo CD WER 60128-50 |
| Continuator 视频 | 无法确认任何可播放链接。Sony CSL 项目页 https://www.sonycsl.co.jp/en/projects/continuator/ 只有图片，Pachet 个人站论文页只有 PDF | | 未找到 |
| Pachet 后续系统可听样例 | Daddy's Car https://www.youtube.com/watch?v=LSHZ_b05W7o ，Flow Composer 演示 https://www.youtube.com/watch?v=f6V8N3ZcSEs ，Lunar 现场录音 https://www.francoispachet.fr/wp-content/uploads/2020/04/LunarPerformance.mp3 | Markov constraints 系列的成品 | 链接取自 Pachet 2020 Flow Machines 论文（arXiv 2006.09232）参考文献，未打开 |
| IDyOM 演示 | https://github.com/mtpearce/idyom/wiki | 无音频，无在线演示，只有 Lisp 代码和教程 | 已读取 |
| Markov chain 音乐演示 | 未找到可信的公开网页演示。ZKM 的 MarkowKetten Explorer 是实体装置 | | 建议：用报告者自己的 144 个数字写一个 Tone.js 页面，现场生成最有说服力 |
| Music Transformer 注意力可视化 | https://magenta.github.io/music-transformer-visualization | 交互钢琴卷帘上的注意力，有 Bach chorale 和钢琴演奏两种样例，页面未明示音频播放 | 已读取 |
| librosa 结构分段示例 | https://librosa.org/doc/0.11.0/auto_examples/plot_segmentation.html | 代码和图，无播放器，可现场跑 | 已读取 |

---

## G. 大脑部分的统一故事

**主题（一句话）：大脑和生成模型都是下一个事件的预测器，所以检验"模型里有没有结构"的办法不用懂乐理，把模型的预测或中间表示拿去解释脑信号就行，语言上已经走通，音乐正在走同一条路。**

讲述顺序（每条一句，标注是否含图）：

1. Kell et al. 2018, Neuron（无图）。为识别语音和音乐而训练的网络能预测听觉皮层 fMRI，中间层对应初级皮层，深层对应非初级区，第一次把"任务驱动网络"和听觉皮层层级对上。
2. Schrimpf et al. 2021, PNAS（无图）。语言模型越会预测下一个词，越能预测人脑对句子的反应，预测是大脑和模型共同的组织原则。
3. Caucheteux and King 2022, Communications Biology（无图）。102 人 fMRI 和 MEG，模型与脑的相似度主要由"根据上下文预测词"的能力决定。
4. Goldstein et al. 2022, Nature Neuroscience（无图）。ECoG 显示大脑在词到来之前就预测它，之后计算惊讶，并用上下文相关的表示，三条原则与自回归模型共享。
5. Tuckute et al. 2024, Nature Human Behaviour（无图）。反过来用模型挑句子，能按预测驱动或压制语言网络的活动，说明模型不只是拟合，还能控制。
6. Di Liberto et al. 2020, eLife（有图：IDyOM 变阶 Markov）。听 Bach 旋律时，IDyOM 给出的 surprise 和 entropy 在声学之外额外解释脑电，效应约 200 毫秒，20 人中 16 人成立，d = 1.64，ECoG 定位在 planum temporale。这是"一个图能对接大脑"的直接证据。
7. Bellier et al. 2023, PLOS Biology（无图）。29 名癫痫病人 2,668 个电极，从听觉皮层活动反向重建 Pink Floyd，非线性模型 r² 0.429 对线性 0.325，证明脑信号里保留了足够重建的音乐信息。
8. Denk et al. 2025, Nature Communications（无图）。把 fMRI 映射到 MusicLM 的嵌入空间，用检索或生成重建音乐，体裁、乐器和情绪能对上，并用编码模型把 MusicLM 各组件对应到脑区。
9. Pepino et al. 2025, arXiv（无图）。36 个音频模型，下游任务越好的模型与听觉皮层 fMRI 越像（r 大于 0.7），而且相似性在预训练早期就出现。
10. Noguchi et al. 2026, arXiv 2603.03190（无图，但它用的正是 MusicGen 的 next token 概率）。把 MusicGen large 的 surprisal 和 entropy 作为教师信号预训练 EEG 编码器，10 首歌识别准确率从 0.823 升到 0.887，期待特征和声学特征互补。

落点：第 6 条用的是显式图（Markov），第 10 条用的是 MusicGen 的隐式概率。报告者的工作把两者接起来：从 MusicGen 里读出显式的 12 节点图，再用同样的脑电方法判断这张图是不是模型真正在用的东西。

---

## H. 未能核实的内容

- 被工具拦截未能打开的页面：ai.honu.io/papers/musicgen，google-research.github.io/seanet/brain2music，journals.plos.org 的 Bellier 文章页（含 S Audio 下载），github.com/facebookresearch/audiocraft，francoispachet.fr/continuator/continuator.html，所有 YouTube 链接。上述 URL 的存在均由其他已读页面间接确认（见 F 节）。
- Illiac Suite 第四乐章使用 Markov chain：来自 Wikipedia 和 OpenCulture，未查原书。
- Addessi and Pachet 2005 儿童研究：只在 Pachet 2020 论文参考文献中见到，未读原文。
- Castellon et al. 2021 的 ISMIR 2021 venue：arXiv 页未标注，按用户给定接受。
- Ostuni/Oramas TIST 文章的卷号与年份（2016 在线，2017 卷 8）未核实。Pearce 2018 的卷页未核实。
- Moss et al. 2019 PLoS One 作者列表未核实（PubMed 页面未显示）。
- Jeong 2019 乐谱图的具体边类型未从原文核实，上表描述来自摘要和常识。
- Denk et al. 2025 的 7 位作者名单来自 arXiv 版，Nature Communications 版标题为 "Text-to-music generation models capture musical semantic representations in the human brain"，2025 年 11 月 29 日发表，与 arXiv "Brain2Music" 是同一工作（DOI 10.1038/s41467-025-66731-7 在 arXiv 页列出）。
- Noguchi 2026 的提交日期页面未显示。
- "从激活中读出的状态转移图"在音乐生成模型上未检索到已有工作，可能存在漏检。

---

## Sources（每行一条）

Illiac Suite, Wikipedia: https://en.wikipedia.org/wiki/Illiac_Suite
Hear the First Composition Created by a Computer, OpenCulture: https://openculture.com/2019/02/hear-the-first-composition-created-by-a-computer.html
Conklin and Witten 1995, Multiple viewpoint systems for music prediction: https://code.soundsoftware.ac.uk/publications/193
Pachet 2003, The Continuator: https://www.francoispachet.fr/?p=4360
Sony CSL Continuator project page: https://www.sonycsl.co.jp/en/projects/continuator/
Pachet and Roy 2011, Markov constraints: https://link.springer.com/article/10.1007/s10601-010-9101-4
Papadopoulos, Roy, Pachet 2014, Avoiding Plagiarism in Markov Sequence Generation: https://ojs.aaai.org/index.php/AAAI/article/view/9126
Pachet 2020, Assisted music creation with Flow Machines: https://arxiv.org/pdf/2006.09232
Pearce 2005 PhD thesis: https://openaccess.city.ac.uk/id/eprint/8459/
Pearce 2018, Statistical learning and probabilistic prediction in music cognition: https://code.soundsoftware.ac.uk/publications/194
IDyOM wiki: https://github.com/mtpearce/idyom/wiki
Karystinaios et al. 2020, Music genre descriptor based on Tonnetz trajectories: https://jim2020.sciencesconf.org/data/pages/KARYSTINAIOS_E._GUICHAOUA_C._ANDREATTA_M._BIGO_L._BLOCH_I._Music_Genre_Descriptor_1.pdf
Bergomi, Baratè, Di Fabio, Towards a topological fingerprint of music: https://arxiv.org/pdf/1602.00739
Liu, Tse, Small 2010, Complex network structure of musical compositions: https://ideas.repec.org/a/eee/phsmap/v389y2010i1p126-132.html
Ferretti, On the Modeling of Musical Solos as Complex Networks: https://arxiv.org/pdf/1610.00468
Buongiorno Nardelli 2020, Tonal harmony and the topology of dynamical score networks: https://arxiv.org/abs/2006.01033v1
Moss et al. 2019, Statistical characteristics of tonal harmony, Beethoven string quartets: https://pubmed.ncbi.nlm.nih.gov/31170188/
Park et al. 2015, Topology and evolution of the network of western classical music composers: https://epjds.epj.org/articles/epjdata/abs/2015/01/13688_2015_Article_39/13688_2015_Article_39.html
Serrà et al. 2012, Measuring the evolution of contemporary western popular music: https://www.arxiv.org/abs/1205.5651
McFee and Ellis 2014, Analyzing Song Structure with Spectral Clustering: https://archives.ismir.net/ismir2014/paper/000319.pdf
librosa Laplacian segmentation example: https://librosa.org/doc/0.11.0/auto_examples/plot_segmentation.html
Jeong et al. 2019, Graph Neural Network for Music Score Data: https://proceedings.mlr.press/v97/jeong19a.html
Karystinaios and Widmer 2022, Cadence Detection using GNNs: https://arxiv.org/pdf/2208.14819
Karystinaios and Widmer 2024, GraphMuse: https://ismir2024program.ismir.net/poster_142.html
Ostuni, Oramas et al., Sound and Music Recommendation with Knowledge Graphs: https://sisinflab.poliba.it/publications/sound-and-music-recommendation-with-knowledge-graphs/
Jayakumar and Özoğlu 2025, Graphs are everywhere, in music recommendation too: https://arxiv.deeppaper.ai/papers/2504.02598v2
Huang, Dinculescu, Vaswani, Eck 2018, Visualizing Music Self-Attention: https://research.google/pubs/visualizing-music-self-attention/
Music Transformer visualization page: https://magenta.github.io/music-transformer-visualization
Wilkins et al. 2014, Network science and the effects of music preference on functional brain connectivity: https://core.ac.uk/download/345081356.pdf
Copet et al. 2023, Simple and Controllable Music Generation, NeurIPS: https://proceedings.neurips.cc/paper_files/paper/2023/hash/94b472a1842cd7c56dcb125fb2765fbd-Abstract.html
Copet et al. 2023, arXiv PDF v3: https://arxiv.org/pdf/2306.05284v3
MusicGen small model card: https://huggingface.co/facebook/musicgen-small/raw/afd2025357b07ac2f989a8938cbe6dd2ac494f31/README.md
facebook/MusicGen Space README: https://huggingface.co/spaces/facebook/MusicGen/raw/refs%2Fpr%2F2/README.md
Castellon, Donahue, Liang 2021, Codified audio language modeling: https://arxiv.org/abs/2107.05677v1
Wei, Freeman, Donahue, Sun 2024, Do Music Generation Models Encode Music Theory: https://arxiv.org/pdf/2410.00872
Di Liberto et al. 2020, Cortical encoding of melodic expectations, eLife: https://elifesciences.org/articles/51784
Bellier et al. 2023, Music can be reconstructed from human auditory cortex activity (eScholarship PDF): https://escholarship.org/content/qt4ms6t5cv/qt4ms6t5cv.pdf?t=s0ii04
Bellier et al. 2023, Knight Lab publication page: https://knightlab.neuro.berkeley.edu/publication/2024/3/5/music-can-be-reconstructed-from-human-auditory-cortex-activity-using-nonlinear-decoding-models
ScienceDaily on Bellier et al.: https://sciencedaily.com/releases/2023/08/230815151112.htm
Denk et al., Brain2Music arXiv: https://arxiv.org/abs/2307.11078v1
Denk et al. 2025, Nature Communications (Nature Index record): https://www.nature.com/nature-index/article/10.1038/s41467-025-66731-7
NITech news on the Nature Communications paper: https://www.nitech.ac.jp/eng/news/2026/14107.html
Kell et al. 2018, Neuron: https://cbmm.mit.edu/publications/task-optimized-neural-network-replicates-human-auditory-behavior-predicts-brain
Schrimpf et al. 2021, PNAS: https://cbmm.mit.edu/publications/neural-architecture-language-integrative-modeling-converges-predictive-processing
Caucheteux and King 2022, Communications Biology: https://doaj.org/article/6f8ac33012674bcab4e30674755ccd23
Goldstein et al. 2022, Nature Neuroscience: https://research.google/pubs/shared-computational-principles-for-language-processing-in-humans-and-deep-language-models/
Tuckute et al. 2024, Nature Human Behaviour: https://dspace.mit.edu/handle/1721.1/153265
Pepino et al. 2025, Better audio representations are more brain-like: https://arxiv.deeppaper.ai/papers/2511.16849v1
Noguchi et al. 2026, Expectation and Acoustic Neural Network Representations Enhance Music Identification from Brain Activity: https://arxiv.org/html/2603.03190v2
