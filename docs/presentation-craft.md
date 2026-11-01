# 演讲技巧研究：让 45 分钟技术报告每分钟都抓人


证据分级说明：⭐⭐⭐ 有多项实验或元分析支持，⭐⭐ 有单项或小样本实验，⭐ 是资深从业者共识或理论推演，没有实验证据。所有引文均已核对原文，未核对到的一律改为转述并注明。

---

## A. 十条核心原则

**1. 一句话主线（throughline），全场所有内容都为它服务**
机制：工作记忆有限，听众只能带走一个想法。多个并列信息互相干扰，一个想法反复强化才能存留。
来源：Chris Anderson，TED Talks 及 TED 演讲 "TED's secret to great public speaking"，原话 "limit your talk to just one major idea"。Peyton Jones 的提法是 "If the audience remembers only one thing"。Duarte 的 Big Idea 要求三要素：独特立场、利害关系（stakes）、完整句子，并用这句话过滤每一张幻灯片。
幻灯片上的样子：主线写成一句不超过 15 个词、带反常识感的完整句子，例如 "Generative models for language and music carry a hidden graph, and reading it predicts when they fail"。这句话在第 2 分钟出现一次，中段每个 section 结束时以不同形式回到它，结尾再回来。它不是标题，是论点。

**2. 先开缺口，再填缺口（information gap）**
机制：Loewenstein 1994 把好奇心定义为 "a form of cognitively induced deprivation that arises from the perception of a gap in knowledge"（已核对摘要原文）。关键推论：听众先要知道自己缺什么，才会想要你的答案。Heath 兄弟概括为 "we need to open gaps before we close them"。
证据：⭐⭐ 好奇心理论有大量实证，但"演讲中开缺口提升注意力"本身没有直接实验。
来源：Loewenstein 1994 Psychological Bulletin，Made to Stick（Unexpected 一章），Anderson 的第二条 "give your listeners a reason to care"。
幻灯片上的样子：开场不放背景，放一个听众无法立刻回答的具体问题。例如一张只有两个 token 的激活图和一行字 "These two edits look identical from outside. One silently broke the model. Which one?" 下一张不给答案，先说 "by minute 30 you'll be able to tell"。

**3. 反差驱动注意力：what is 与 what could be 来回切换**
机制：Duarte 分析 MLK "I Have a Dream" 和 Jobs 2007 iPhone 发布会，发现两者都在"现状"与"可能的未来"之间反复摆荡，像逆风航行时的 tacking，每次切换都重新拉回注意力，结尾落在"新的世界"。Gregor Hohpe 把它改造成技术报告版：纵轴从 logos（内容基线）到 pathos（兴奋点），三种波形 Pulse（短促尖峰后回落）、Stereo（一条贯穿的例子线并行）、Sawtooth（逐步升温后重置）。
证据：⭐ 这是对成功演讲的事后分析，不是对照实验。
来源：Duarte "The secret structure of great talks"，Resonate，Hohpe "Presenting: the waveform"。
幻灯片上的样子：每个 section 都是一对幻灯片：左边"今天我们做知识编辑/音乐生成是黑箱，失败是静默的"，右边"如果模型内部有一张可读的图，失败就能被看见"。整场 45 分钟至少摆荡 4 到 5 次，不是开头说一次动机就不再回来。

**4. 听众是主角，讲者是导师**
机制：人只对与自己有关的事保持注意。Duarte 原话 "You're not Luke Skywalker. You're Yoda"，"The audience is the hero of our idea"。McEnerney 的写作课把同一件事说得更狠：价值不在你的新颖，而在读者脑中，要回答的是"谁在乎"。
来源：Duarte Resonate 与 TEDxEast 演讲，McEnerney "The Craft of Writing Effectively"。
幻灯片上的样子：跨子领域听众面前，每个结果后面跟一张"如果你做 X，这意味着 Y"：做系统的人看到的是可监控的失败信号，做 HCI 的人看到的是可解释的生成控制，做理论的人看到的是结构推断问题。合作外联的目标本身就要求这一条。

**5. 断言加证据，不是话题加要点（assertion-evidence）**
机制：标题写成完整句子的论断，正文用视觉证据支撑，听众在 3 秒内知道这张幻灯片要证明什么，不必自己从要点里拼结论。
证据：⭐⭐ Alley 等 2006（Virginia Tech 地学课，四个学期共约 740 名学生）：句子标题幻灯片对应题目的回忆率 79% 对 69%，p<0.001，但作者自称 pilot，讲课非完全一致。Garner & Alley 2013（n=55 对 56，6 分钟 MRI 讲解）：一周后延迟测试综合理解题 2.17 对 1.84，p=0.038，即时测试整体差异不显著，次要数字的回忆反而 T-S 组更高（69% 对 39%），因为那些数字只出现在 T-S 幻灯片上。几乎所有研究都出自 Alley 本人团队。Farkas 的批评：对照组用的是糟糕的常规幻灯片而非设计良好的要点式幻灯片，所以显著结果"出奇地小"，且强制每条论断配一张图会产生无用的小图。
来源：Alley "The Craft of Scientific Presentations"，Garner & Alley 2013 ASEE / IJEE，Farkas 评估论文，Doumont "One message per slide. One slide per message."
幻灯片上的样子：不写 "Results on knowledge editing"，写 "After a silent failure, the activation graph loses its hub structure within three layers"，下面只放那一张图，图里只高亮支持这句话的部分。

**6. 具体例子是主武器，不是抽象框架**
机制：Peyton Jones 原话 "Examples are your main weapon"，"Narrow, deep beats wide, shallow"。Anderson 的第三条 "build your idea, piece by piece, out of concepts that your audience already understands"，工具是隐喻和例子。Heath 的 Concrete 原则同理。
来源：Peyton Jones "How to give a great research talk"，Anderson，Made to Stick。
幻灯片上的样子：整场用一个贯穿的运行例子（一条被编辑的事实，一段被 steering 的音乐），每次讲新方法都先回到这个例子上看它发生了什么，再抽象。时间不够时砍一般性陈述，不砍例子。

**7. 模式打破与"postdictable"的惊讶**
机制：Heath 原话 "The most basic way to get someone's attention is this: Break a pattern." 好的惊讶事后可解释（postdictable），事前不可预测。Cialdini 的说法是先有 "Huh?" 再有 "Aha!"。Winston 的 5S 之一是 Surprise。
来源：Made to Stick，Winston "How to Speak"。
幻灯片上的样子：用 Reveal.js fragment 先显示听众会预期的结果（比如"更多编辑等于更多损伤"），停一拍，再显示真实曲线（损伤和编辑数量无关，和图结构有关）。惊讶要落在你的核心发现上，不是落在花絮上。

**8. 对结构进行"口头标点"和循环**
机制：注意力的实证研究（Bunce 等 2010，clicker 自报告）发现走神不是 10 分钟后才开始，而是频繁且短促，第一次走神可能在 30 秒内，之后周期越来越短，但演示或提问之后紧接着的讲授段走神显著减少。所以需要定期提供"重新上车"的地标。Winston 原话："provide some landmark places"，"you need to say it three times"。
证据：⭐⭐ Bunce 2010 是自报告，样本为三门化学课。
来源：Winston，Bunce Flens Neiles 2010 J. Chem. Educ.
幻灯片上的样子：每 7 到 10 分钟一张极简的"我们走到哪了"幻灯片，上面不是目录，而是主线句子加一个新填进去的词。每段结束一句口头总结，再抛下一段的问题。

**9. 先给结论（punch line / forecast），再给证明**
机制：会议听众注意力在前几分钟最高，长背景会把它耗尽。Doumont 称之为 "theorem-proof approach, not a chronology"。Mark Hill 的 forecast slide 是报告的"摘要"。Yuki 转述 Michelle Strout 的 punch line method：短版（问题、关键想法、贡献）在前几分钟讲完，再进详细版，并且 punch line 要是 insight 而不是数字（为什么有效比快了多少重要）。
来源：Doumont（Scripps 报道），Mark Hill "Oral Presentation Advice"，Yuki "The Punch Line Method"。
幻灯片上的样子：第 3 到 5 分钟出现一张"今天的三个发现"幻灯片，每条是一句断言。之后 35 分钟是证明。听众中途走神也知道你在证明哪一条。

**10. 结尾落在贡献，不落在 "Thank you" 或 "Questions?"**
机制：结尾决定记忆（Anderson："The way a talk ends is the way the audience will remember it."）。Winston 原话："your final slide should have this label, contributions"，"the last thing you do should not be saying thank you"，"It's a weak move."
来源：Winston，Anderson（七种结尾：camera pull-back、call to action、personal commitment、values and vision、satisfying encapsulation、narrative symmetry、lyrical inspiration），Clayton Scott（Michigan）"不要以请提问结束"。
幻灯片上的样子：最后一张是贡献加合作邀请，回到开场那张图并给出答案（narrative symmetry），然后停在这张上接受提问。

---

## B. 技巧清单（按阶段）

**开场前 90 秒**
- 不要以自我介绍、致谢、目录开场。Doumont：先抓住注意力再介绍自己。Peyton Jones：目录幻灯片 "conveys near zero information at the start of your talk"。Hill 的 outline 可以压缩到标题页底部一行。
- Anderson 的四种开场：一剂戏剧性、点燃好奇、一张震撼的图或物件、tease 但不揭底。Abrahams："像动作片那样开场"，前 60 秒是焦虑高峰也是注意力锚点。
- Winston 的 empowerment promise：原话 "tell people what they're going to know at the end of the hour"。不要以笑话开场。
- Doumont：问题是面向科学听众最好的 attention getter，但必须相关。
- 先说合作者（Winston：开头介绍合作者，不是结尾）。

**建立问题**
- Peyton Jones：你有 2 分钟让听众在乎这个问题（原话 "You have 2 minutes to engage your audience"）。Kumar（Cleveland State）：非专家约 2 分钟内、专家约 5 分钟内会决定是否继续听。
- Olson ABT：AND（共识）BUT（矛盾）THEREFORE（我们做了什么）。AAA 是无叙事的罗列，DHY 是过度叙事的混乱。用 Dobzhansky 模板找唯一主线："Nothing in ___ makes sense, except in the light of ___"。本报告可填 "Nothing in silent editing failures makes sense except in the light of the activation graph"（示例，非引文）。THE 评论指出 ABT 缺最后的 payoff，所以 THEREFORE 后面还要接一个明确的发现。
- McEnerney：用不稳定性词汇（but、however、anomaly、inconsistent）标出问题，文献不是综述而是加深问题。
- McKee：只讲成功既无聊又不可信，原话 "the energy to live comes from the dark side"（HBR 2003）。讲你走过的死胡同。

**讲方法**
- Peyton Jones：密集符号让人睡着，只展示某一具体侧面，其余放 backup。Yuki：整场只放一个公式可以做到。
- Anderson 的解释五步：从听众所在处开始、点燃好奇、概念一次一个、隐喻、例子。
- MIT Comm Lab：先放示意图再放数据，让听众知道该看什么。公式中灰掉次要项提高信噪比。
- Winston 的 fence：原话 "building a fence around my idea"，明确说出你的方法和相邻方法的边界。
- 对跨子领域听众：Heath 的知识诅咒提醒，用"三个为什么"检查每个术语是否真的需要。

**讲结果**
- Hill：解读数字而不是展示数字，避免大表格。Naegle 十规则：一个图一张幻灯片，不讲的细节不要出现在图上，因为听众会盯住所有可见的东西。
- 结果要连回 punch line：每张结果图标题是对三个发现之一的回应。
- Duarte STAR moment（Something They'll Always Remember）：五种形式，可记忆的演示、可复述的短句、唤起性视觉、情感故事、震撼数据。Jobs 第一次演示滚动时听众倒吸一口气。45 分钟里设计一个，最好是现场或录好的 demo。
- Gallo 的 "jaw-dropping moment"（Gates 放蚊子）同理，但他引用的"科学证据"均未具名，当作从业者经验看。

**转场**
- Winston 口头标点。MIT Comm Lab：偶尔用"这页提问、下页回答"，但不要每页都这样。
- Hohpe 的 Stereo 波形：一条运行例子贯穿两个领域（语言、音乐），每次切换领域都通过它过渡。
- 转场时回到主线句子，换一个词。

**结尾**
- Winston：最后一张标 contributions，不说 thank you，可以 "salute the audience"。
- Anderson：narrative symmetry（回到开场的图、问题、物件并闭合）。
- Peyton Jones："Absolutely without fail, finish on time"。超时就砍，不要问听众能否继续。
- Doumont：判断结尾好坏的标准是最后一个词落下后掌声来得多快。
- 合作外联场合：最后一张列出 2 到 3 个明确的"我需要谁"，比"欢迎合作"具体得多。

---

## C. 从电影和剧本借来的手法

| 手法 | 影视里的定义 | 映射到报告 | Reveal.js 实现 |
|---|---|---|---|
| Trailer | 三幕：setup、rising conflict、climax montage，展示最震撼的画面但不泄露主要剧情点，常以 cast run 和日期收尾 | 开场 60 到 90 秒放 4 到 6 张图的快速连播：语言模型的一张图、音乐模型的一张图、一个失败案例、一句主线，不解释，只建立"今天会发生什么" | 用 `data-autoslide` 做定时自动翻页的一组 section，或一张幻灯片内多个 fragment 快速 fade-in，配 `data-background-video` |
| Cold open | 片头前直接进入动作，建立人物、冲突、基调，制造悬念但不解决，喜剧把最大的笑点放在 cold open 末尾 | 第一张不是标题页，是那个未解的案例。标题页放在第 3 张 | 把 title slide 移到 cold open 之后，cold open 用 `data-transition="none"` 显得干净 |
| Open loop | 悬念不闭合，让观众带着问题往下看。理论依据常引 Zeigarnik 效应，但该效应的复制结果不一致（Simply Psychology 综述），不要在报告里拿它当科学依据 | 开场抛的问题到第 30 分钟才答。中段再开两个小 loop，每个 10 分钟内闭合 | 做一张 "open questions" 幻灯片，每闭合一个就用 `fragment strike` 或 `fragment highlight-current-*` 划掉或点亮一条 |
| Setup and payoff | Chekhov 原则，第一幕挂的枪后面必须响。先定 payoff 再反推 setup，payoff 要给 setup 新的意义而不是重复它 | 第 5 分钟随口提一个"无关"的观察（比如音乐模型里也看到了同一种 hub 结构），第 35 分钟它成为语言和音乐统一的关键证据 | `data-auto-animate` 让第 5 分钟那张图在第 35 分钟原样飞回来并变换位置，视觉上告诉听众"这是同一个东西" |
| Reveal timing | Masterclass：建立悬念但不解决，喜剧最大笑点放在段落末尾。Heath：惊讶必须 postdictable | 每段结果的关键曲线最后出现，先出坐标轴和基线，再出预期曲线，最后出真实曲线 | 三个 fragment 按 `data-fragment-index` 排序，最后一个用 `fade-up` 或 `grow` |
| Rhythm / cutting | Murch 的 Rule of Six：情感 51%，其次故事、节奏、视线、二维、三维。原话 "don't ever give up emotion before story"。Cutting on action 利用动作中的切点掩盖剪辑痕迹 | 节奏：浓密的方法段之后紧跟一张只有一句话或一张图的幻灯片，让人喘息。切点：在听众正在"动作"（刚被问了问题、刚笑完）时切换话题，而不是说完一段再切 | 交替使用高密度与近空白幻灯片，空白页用大字号单句，`transition="fade"` 比 `slide` 更像电影剪辑 |
| Eye trace | Murch 的第四条，剪辑时保持观众视线落点连续 | 连续两张图里，关键元素位置不变，变化只在一个维度 | `data-auto-animate` 匹配 `data-id`，只有变化的元素动 |
| Show, don't tell | 演示优于描述 | 能放 demo 的地方不放 bullet，能放音频的地方放音频（音乐生成天然有这个优势） | 嵌入 audio 元素，fragment 控制播放时机 |

注：本次会话无法抓取 revealjs.com 的 fragments 与 auto-animate 文档页和 GitHub 仓库页（权限请求超时），上表 Reveal.js 功能基于我对其标准文档的了解：fragment 类有 fade-in、fade-out、fade-up/down/left/right、fade-in-then-out、fade-in-then-semi-out、grow、shrink、strike、highlight-red/green/blue、highlight-current-*、semi-fade-out、current-visible，`data-fragment-index` 控制顺序，`data-auto-animate` 按 `data-id` 匹配元素，代码块用 `data-line-numbers="1|3-5"` 分步高亮。建议他自行对照当前版本文档确认。

---

## D. 幻灯片形式规则

**标题**
- 完整句子断言，左对齐，最多两行，约 28 点（Alley / Northeastern 指南）。Doumont 的例子：不写 "The Distribution of Stars"，写 "M Dwarfs are the Most Common Type of Star"。
- 不用 "Outline"、"Results"、"Background" 这类泛标题。

**一页一念**
- Doumont："One message per slide. One slide per message."。Naegle：约每分钟一张，45 分钟约 40 到 45 张（含极简过渡页），每页不超过 6 个元素。Hill 的说法是每张约两分钟（不含标题和目录页），两者差异来自密度，选一种并保持一致。
- Duarte 三秒 glance test：三秒内看不出这页在说什么就重做。

**文字上限**
- Alley：听众每分钟阅读不超过 20 个词，正文段落不超过两行，列表 2 到 4 项且不用项目符号而用间距。
- Duarte：超过 75 个词是文档（slideument），约 50 个词就变成提词器。
- Mayer 冗余原则（⭐⭐⭐）：屏幕文字与口头叙述逐字相同会降低学习。Yue, Bjork & Bjork 2013 的细化：缩短并改写的文字优于逐字相同，差异过大又会过载，原话 "The captions should be similar to the narration, but they should not be identical."。所以屏幕上写的要是你说的话的压缩改写版，不是讲稿。
- Winston："There are always too many slides, always too many words."

**动画规则**
- 有用：逐步揭示让听众只看到你正在讲的（MIT Comm Lab），有 punch line 的分步揭示（Peyton Jones：无 punch line 就别一条条出 bullet），auto-animate 保持视线连续，先示意图后数据。
- 有害：装饰性过渡，不服务于论点的动效（Clayton Scott、Naegle 第十条）。Mayer 一致性原则（coherence）：无关材料降低学习。
- Mayer 信号原则（⭐⭐⭐）：Alpizar 等 2020 元分析，29 项研究 44 个效应量 2726 人，d=0.38，高质量研究中效应稳定。所以高亮、箭头、变灰是有证据的动效，飞入旋转不是。
- Mayer 分段原则（⭐⭐⭐）：Rey 等 2019 元分析，56 项研究，对保持和迁移小到中等效应，高先验知识者获益更多。对应做法：一张复杂图拆成 3 张递进。

**图**
- 一张幻灯片一个图版（Naegle）。直接标注数据而不用图例（Doumont）。不讲的线删掉或灰掉。重画而不是截论文图。
- 避免红绿对比承载关键信息（Scott，约 5% 男性色盲）。
- 打印 6 页一张检查可读性（Doumont，MIT Comm Lab）。
- 不用激光笔，Winston 原话 "You can't use a laser pointer without turning your head"，用幻灯片内的箭头或走到屏幕前指。

**数字**
- Hill：解读而不是展示。Abrahams：让统计数字"人化"，绑到一个场景或一个后果。
- 每页最多一个需要记住的数字，写在图旁边。
- Peyton Jones：不为结果道歉。

**Winston 的 hapax legomenon**：有且只有一次可以用一张让人等着你解释的复杂图，原话 "you can get away with exactly once in your presentation"。

---

## E. 常见误区与被高估的建议

1. **"注意力 10 到 15 分钟就掉"**：Wilson & Korn 2007 和 Bradbury 2016 均指出该说法缺乏原始数据，最常被引的源头几乎不讨论注意力，Bradbury 原话 "the available primary data do not support the concept of a 10- to 15-min attention limit"，最大的变异来源是讲者本人。Bunce 2010 更接近真相：走神频繁且短促，从 30 秒就开始，但换节奏（演示、提问）后立刻下降。结论不是"每 10 分钟换活动"，而是"每几分钟给一次回来的理由"。
2. **"18 分钟规则"与"cognitive backlog"**：Gallo 书中引用的"科学证据"均未具名，TED 的 18 分钟是策展决定不是认知常数。45 分钟部门报告不必硬切成三个 18 分钟。
3. **Guo 等 2014 的 6 分钟 MOOC 发现**：690 万次观看，中位参与时长不超过 6 分钟，9 分钟以上视频常看不到一半。但这是自选人群、异步视频、参与度而非学习，不能直接套到现场报告。可借鉴的部分是语速与热情相关的参与度（语速快的段落参与度最高可达 2 倍，作者归因于热情），与 Peyton Jones "By far the most important thing is to be enthusiastic" 一致。
4. **Zeigarnik 效应作为 open loop 的科学依据**：原始研究样本小、无预注册，后续复制结果不一致。open loop 作为技巧有效（从业者共识），但别在报告或写作里把它当心理学定律引用。
5. **Tufte 的 PowerPoint 批判**：他对要点式层级、低分辨率、Columbia 幻灯片的批评有价值（"festival of bureaucratic hyper-rationalism"），但 Norman 的反驳也成立：问题在报告不在工具，原话 "the problem is with the talk, not with the tool"。Norman 的实用方案是三份材料：自己的笔记、给听众看的图、会后发的 handout，"Don't confuse one for another"。对一个合作外联报告，handout 可以是一页 PDF 的项目摘要加联系方式。
6. **assertion-evidence 的"显著更好"**：见 A5，效应真实但小，且对照组弱，主要出自同一团队。采用它的理由是逻辑清晰和强迫讲者先想清楚（Aippersbach 2013 发现 A-E 组讲者自己对内容理解更好，这一点对准备过程最有价值），不是因为它"被证明"大幅提升听众记忆。
7. **"每条断言必须配一张图"**：Farkas 批评这会产生无用的小图。主线句子页、转场页可以只有文字。
8. **"图片优于文字"的 picture superiority effect**：Reynolds 的书常被引述此效应，但本次检索到的 Reynolds 笔记页并未提及该效应，不要把它归于他。Mayer 多媒体原则（文字加图优于纯文字）有证据，但前提是图承载信息而非装饰。
9. **用 slide 当讲稿和当讲义**：Reynolds 的 slideument 概念，Winston 原话 "I think they're for exposing ideas, not for teaching ideas"。
10. **结尾 "Questions?" 页**：Winston 和 Scott 都指出它让掌声无处落。

---

## F. 单页逐张检查表

对每一张幻灯片问：
1. 标题是一句可以被反驳的断言吗？去掉正文只看标题，能复述这页的结论吗？
2. 三秒内能看出这页在说什么吗？
3. 这页在证明三个 punch line 中的哪一条？说不出来就删或并入过渡页。
4. 屏幕上的词是我要说的话的压缩改写，不是逐字稿？不超过约 20 个词每分钟停留时间？
5. 图里有任何我不会亲口提到的线、轴、图例、数字吗？有就灰掉或删。
6. 关键元素有高亮或箭头吗（信号原则）？用了飞入旋转之类无信息的动效吗？
7. 这一页和上一页之间，视线落点连续吗？变化只在一个维度吗？
8. 这页有没有开一个问题或闭合一个问题？连续三页都没有就插一页。
9. 这页跨子领域的同事能听懂吗？每个术语是否在前面用例子或隐喻建立过？
10. 这页离上一次回到主线句子超过 10 分钟了吗？
11. 它是 what is 还是 what could be？连续五页都在同一侧就该切换。
12. 删掉这页，报告会变差吗？不会就删。

对整场问：
- 前 90 秒有未解的具体案例、有 empowerment promise、没有目录没有自我介绍吗？
- 第 5 分钟前出现了三个发现的 forecast 吗？
- 有一个 STAR moment 吗？它落在核心发现上吗？
- 第 5 分钟埋的 setup 在第 35 分钟 payoff 了吗？
- 最后一页是 contributions 加明确的合作请求，并回到开场的图吗？
- 公式数量是否不超过 1 到 2 个？backup 里有细节吗？
- 能在 45 分钟内 "Absolutely without fail, finish on time" 吗？

---

## G. 来源

Patrick Winston, How to Speak, MIT OCW 官方字幕 https://www.ocw.mit.edu/courses/15-371-innovation-teams-fall-2024/Unzc731iCUY_transcript.pdf
Patrick Winston, How to Speak 笔记 https://akos.ma/blog/how-to-speak-by-patrick-winston/
Simon Peyton Jones, How to give a great research talk（幻灯片） https://www2.cs.ucy.ac.cy/courses/EPL670/docs/GivingATalk.pdf
Simon Peyton Jones, Giving a talk handout https://john.cs.olemiss.edu/~hcc/researchMethods/notes/PeytonJones/Giving_talk_handout.pdf
Chris Anderson, TED's secret to great public speaking（字幕） https://rosetta.to/u/ted/ted-s-secret-to-great-public-speaking-chris-anderson-ted?t=0
Chris Anderson, TED Talks 书评与要点 https://francistapon.com/Work/Reviews/guide-book-review-ted-talks-by-chris-anderson/
Chris Anderson, TED Talks 摘要（Shortform） https://www.shortform.com/blog/ted-talks-the-official-guide-to-public-speaking/
Nancy Duarte, The secret structure of great talks https://www.duarte.com/resources/secret-structure-great-talks/
Nancy Duarte, STAR moment https://www.duarte.com/blog/secret-to-unforgettable-events-and-memorable-speeches/
Nancy Duarte, Big Idea https://www.duarte.com/blog/how-to-develop-the-best-big-idea-for-your-presentation/
Nancy Duarte, Glance Test https://www.duarte.com/resources/slide-glance-test/
slide:ology 笔记 https://chrischow.github.io/booknuggets/2020/01/23/2020_07-slideology.html
Resonate 摘要（Blinkist） https://www.blinkist.com/en/books/resonate-en
Gregor Hohpe, Presenting: the waveform（Sparklines 2.0） https://architectelevator.com/strategy/presenting-waveform/
Randy Olson, Houston We Have a Narrative 书评（IAN UMCES） https://ian.umces.edu/blog/randy-olsons-new-book-houston-we-have-a-narrative/
Randy Olson, ABT 工作坊材料（TAMUCC） https://gradcollege.tamucc.edu/grow/assets/documents/abt-framework-intro-workshop.pdf
Houston We Have a Narrative 书评（Times Higher Education） https://www.timeshighereducation.com/books/review-houston-we-have-a-narrative-randy-olson-university-of-chicago-press
Made to Stick 笔记 https://www.nateliason.com/notes/made-stick-chip-dan-heath
Loewenstein 1994, The Psychology of Curiosity（摘要） https://stafforini.com/works/loewenstein-1994-psychology-curiosity-review/
Robert McKee, Storytelling That Moves People（HBR 2003） https://www.bridge2employment.org/wp-content/uploads/2020/03/Storytelling-That-Moves-People_Article.pdf
McKee 的 gap 概念解读 https://writerunboxed.com/?p=27562
Jean-luc Doumont 演讲报道（Scripps） https://www.scripps.edu/newsandviews/e_20060515/presentation.html
Doumont 一页一念（AstroBetter） https://www.astrobetter.com/learning-to-give-better-talks-one-message-per-slide-one-slide-per-message/
Doumont 三定律 https://thinkdev.org/blog/doumonts-laws-of-communication
Garr Reynolds Presentation Zen 笔记 https://www.antoinebuteau.com/lessons-from-garr-reynolds/
Carmine Gallo, Talk Like TED 要点 https://www.carminegallo.com/cracking-the-ted-code-takeaways-from-talk-like-ted-the-9-public-speaking-secrets-of-the-worlds-top-minds/
Matt Abrahams, Think Fast Talk Smart 笔记 https://www.antoinebuteau.com/lessons-from-matt-abrahams.md
Larry McEnerney, The Craft of Writing Effectively 笔记 https://buomsoo-kim.github.io/learning/2020/03/30/Craft-of-writing-effectively.md
Edward Tufte, Cognitive Style of PowerPoint 讨论（GovExec 转载） https://www.edwardtufte.com/?p=460
Tufte 论点摘要 https://www.rightattitudes.com/2016/06/10/the-cognitive-style-of-powerpoint
Don Norman, In Defense of PowerPoint https://jnd.org/in-defense-of-powerpoint/
Michael Alley 团队研究列表（PSU） https://writing.engr.psu.edu/research.html
Alley et al. 2006, Testing the effect of sentence headlines https://peer.asee.org/testing-the-effect-of-sentence-headlines-in-teaching-slides.pdf
Garner & Alley 2013, Assertion-evidence slides appear to lead to better comprehension https://peer.asee.org/assertion-evidence-slides-appear-to-lead-to-better-comprehension-and-recall-of-more-complex-concepts.pdf
Garner & Alley 2013 二手摘要（WUSTL CTL） https://ctl.wustl.edu/in-powerpoint-its-the-headline-that-makes-the-difference/
David Farkas, Assessment of Alley's slide design https://faculty.washington.edu/farkas/dfpubs/Farkas-Assessment%20Of%20Alleys%20Slide%20Design.pdf
Assertion-evidence 幻灯片指南（Northeastern） https://course.khoury.northeastern.edu/cs7976f19/Materials/Slide-guidelines.html
MIT Comm Lab, Slide Design https://mitcommlab.mit.edu/nse/commkit/slide-design
Naegle 2021, Ten simple rules for effective presentation slides https://www.ayoob.csb.pitt.edu/wp-content/uploads/2023/10/10-Simple-rules-for-effective-presentation-slides-Naegle-1.pdf
Mark Hill, Oral Presentation Advice https://pages.cs.wisc.edu/~markhill/conference-talk.html
Tomofumi Yuki, The Punch Line Method https://people.irisa.fr/Tomofumi.Yuki/pline.html
Clayton Scott, Advice on giving a research talk https://web.eecs.umich.edu/~cscott/talk_advice.htm
Sathish Kumar, Creating an Effective Research Talk https://www.csuohio.edu/sites/default/files/Creating%20an%20Effective%20Research%20Talk.pdf
Bradbury 2016, Attention span during lectures: 8 seconds, 10 minutes, or more? https://pubmed.ncbi.nlm.nih.gov/28145268/
Wilson & Korn 2007 摘要（Faculty Focus） https://www.facultyfocus.com/articles/instructional-design/student-attention-spans
Wilson & Korn 2007 摘要（Glessmer） https://mirjamglessmer.com/2014/10/01/development-of-student-attention-over-time/
Bunce, Flens & Neiles 2010 摘要（Faculty Focus） https://www.facultyfocus.com/articles/teaching-and-learning/students-attention-interesting-analysis/
Guo, Kim & Rubin 2014, How video production affects student engagement https://www.cs.rochester.edu/hci/pubs/pdfs/edX-MOOC-video-production-and-engagement_LAS-2014.pdf
注意力神话溯源（Texas State） https://ideabook.wp.txstate.edu/?p=195
Mayer 12 原则（Dartmouth） https://services.dartmouth.edu/TDClient/1806/Portal/KB/PrintArticle?ID=171655
Alpizar, Adesope & Wong 2020, 信号原则元分析 https://rex.libraries.wsu.edu/esploro/outputs/journalArticle/A-meta-analysis-of-signaling-principle-in/99900601052901842
Rey et al. 2019, 分段效应元分析 https://is.mpg.de/publications/rey2018segmenting
Yue, Bjork & Bjork 2013, Reducing verbal redundancy https://sites.lifesci.ucla.edu/psych-bjorklab/wp-content/uploads/sites/13/2016/07/YueBjorkBjork2013_redundancy.pdf
Zeigarnik 效应证据综述 https://www.simplypsychology.com/articles/zeigarnik-effect-unfinished-tasks
Walter Murch, Rule of Six https://nofilmschool.com/2016/11/6-rules-good-cutting-according-oscar-winning-editor-walter-murch
Cold open 定义（Masterclass） https://www.masterclass.com/articles/what-is-a-cold-open
Setup and payoff（Final Draft） https://www.finaldraft.com/blog/how-to-put-setups-and-payoffs-in-your-scripts
Trailer 结构（Masterclass） https://www.masterclass.com/articles/how-to-make-a-movie-trailer

未能抓取的页面（权限请求超时，内容基于已有知识，建议自行核对）：https://revealjs.com/fragments/ 、https://revealjs.com/auto-animate/ 、https://github.com/hakimel/reveal.js

未核实项说明：Murch 六条规则除"情感 51%"外的具体百分比未在抓取页面中确认。Gallo 书中引用的神经科学证据均未具名。McKee "gap" 概念本次只拿到二手解读，无原文引文。Doumont "Trees, Maps, and Theorems" 的三定律来自二手页面，其中 "message vs topic" 区分未在该页出现。
