# 讲者备忘：每篇论文讲什么，被问到怎么答

适用于 2026-11-19 系内报告 "Is There a Graph Inside Generative Models?"。页码会随每轮修改变化，以幻灯片标题为准。数字都已经过核对（核对来源见 idea-funnel 运行记录 critique_fable.md），标"待查"的还没核实，讲的时候不要说死。

## 一、我们自己的工作（最容易被追问）

### 1. Delta-Graph Signatures（SDM 2026，第 3、13 到 16 页）
**一句话**：编辑前后各记录一遍模型内部每个模块的活动，把"哪些模块一起动"画成图，两张图相减就是 delta graph，用它的形状给编辑排风险。

**打个比方**：体检只问"你感觉好吗"（考试只看答案），我们拍一张"术前术后的神经连接图"，看哪里重新接了线。

**做法**
- 节点：每层一个注意力块、一个 MLP 块，共 2L 个。
- 输入：每个事实 12 条探针提示词，和编辑、评测用的提示词不重叠。
- 边：偏相关（partial correlation），也就是排除其他模块的影响后，两个模块是否还一起变化。用岭回归（ridge）估计，编辑前后用同一个 λ，这样两张图可比。
- 特征：变化有多大、多集中、在哪一层，以及谱特征：把"每个节点变了多少"投到编辑前那张图的拉普拉斯特征向量上。低频代表变化在全网平滑铺开，高频代表局部的一个结。
- 风险分：在先验（编辑器加模型）上加 delta graph 特征，跑 L2 逻辑回归。

**主要结果**：1,761 个"考试全过"的编辑里，56%（987 个）换个说法问就失败。同样只抽查 20%，随机找到约 11 个坏编辑，按编辑器和模型挑 14 个，用 delta graph 17 个。AUC 从 0.703 升到 0.797（正文 Table 5.1）。消融实验：只看变化大小几乎等于随机（0.52 到 0.59），起作用的是形状。

**会被问的问题**
- *"12 条提示词估计 2L 乘 2L 的偏相关矩阵，样本不够，矩阵是奇异的。"* 答：所以用岭回归，它给出稳定的精度矩阵估计。我们关心的不是单条边的绝对值，而是同一个估计器在编辑前后的差。要准备的补充：有没有用随机提示词做零分布对照（查论文附录，没有就说是下一步）。
- *"这能用在剪枝、合并、去学习上吗？"* 答：论文只验证了知识编辑，其他手术是假设，第 10 页的意思是"它们都面临同样的检测问题"，不是"我们已经解决了"。
- *"0.797 不算高。"* 答：它是分诊工具，不是裁判，价值在于先查谁。风险最高的 20% 里 86% 真的失败，其余 80% 里是 49%。
- *"为什么不用 SAE 或探针？"* 答：那些读的是一个向量方向，我们读的是模块之间关系的变化，两者互补。

### 2. 多跳 KGQA 诊断（CIKM 2026，第 9 页）
**一句话**：多跳问答在第二跳普遍掉下悬崖，其中一部分不是模型笨，而是知识图谱里根本没有那条路径。论文给出判断条件和修补方法。

**关键概念**
- 类型同态（typed homomorphism）：把问题的结构（病人到入院到过敏）映射到病历图里，节点类型和边类型都要对得上。找不到这样的映射，就没有正确答案。
- 四类失败：EF、RF、CompF、OOB。临床数据里的失败全部是 CompF，也就是组合缺边。
- Yannakakis 算法：无环连接查询的经典多项式时间算法，用来构造性地求答案，保证"能答的一定找得到"。

**数字**：MIMIC-III 上 9 个模型（3B 到 1.6T），9 个里有 7 个一跳在 76%，两跳掉到 6% 到 12%，落差 52 到 70 个百分点。1.6T 那个是 DeepSeek-V4-Pro（MoE）。CORAL 上补 51 条边，结构性遗漏从 8.22% 降到 0%。

**会被问的问题**
- *"怎么知道模型没见过 MIMIC？"* 答：不能绝对保证，能说的是 PhysioNet 受限数据，不在任何公开预训练语料里。
- *"51 条边是人工加的吗？"* 答：按 2 个模板补的类型兼容边。具体是人工还是自动，讲之前确认一下。
- *"这和编辑有什么关系？"* 答：它是"图在模型外面"的那一半。知识本身有结构，答不对有时是结构缺了。后面讲"模型里面的图"。

### 3. 音乐的马尔可夫图实验（进行中，第 5、19 到 22 页）
**一句话**：把旋律折叠成 12 个音级，数"哪个音后面跟哪个音"得到 12 乘 12 的表（144 个数），一个普通分类器就能认出旋律来自哪个传统。

**数字**：1,000 首旋律、六个语料库，一阶图 70.9%（随机 17%）。重建后的 992 首上，一阶 70.2%，二阶 78.2%，加上音长的节点 86.8% 到 88.7%。

**会被问的问题**
- *"只用 12 个音级的直方图（不看顺序）能得多少？"* 已补跑（2026-11-04，同样 992 首、同样五折）：只数音符 41.9%，加上顺序（一阶图）70.2%，图多出约 28 个点。加音长时也一样：只数 68.4%，一阶图 86.8%。第 21 页已经放上这个基线。
- *"为什么用逻辑回归而不是 n 元语法的似然分类？"* 答：两种都可以，逻辑回归把 144 个数当特征，好解释。
- *"语料混杂吗？"* 答：有，巴赫众赞歌同一首调子会有多个和声版本，抬高长记忆的分数，帕莱斯特里那和 Trecento 的版本音值较长，抬高音长特征。这两点已经写在备注里。

### 4. 风格的单向 steering（投稿中，第 6、24 页）
**一句话**：在 MusicGen 里减去一个风格方向，很容易让音乐离开这个风格，但加上方向很难让它进入另一个风格。

**规矩**：不说论文标题，不说投稿会议。爵士和古典两个例子标的是示意。

**会被问的问题**
- *"会不会是评判器的阈值问题？"* 答：要准备的对照是同一个评判器在真实爵士和古典片段上的分数，以及逐段的分布，而不只是均值。
- *"这和 Tan 2024 说的'均值方向对单个输入不可靠'是一回事吗？"* 答：不是。Tan 说的是同一个方向对不同输入效果不一，我们说的是同一个风格进出不对称。图的假设是：风格像一个出口多、入口少的岛。

## 二、引用的别人的工作

| 页 | 论文 | 讲了什么 | 可能被问 | 怎么答 |
|---|---|---|---|---|
| 2 | Cohen 等，RippleEdits，TACL 2024 | 改一个事实后，用六类问题检查相关事实有没有跟着变。MEND、ROME、MEMIT 平均只有 38% 到 66% | "有没有方法做得好？" | 论文里上下文编辑（in context）最好，比 ROME 高 10 到 29 个点 |
| 2 | Zhong 等，MQuAKE，EMNLP 2023 | 编辑后的多跳问题，模型普遍失败 | "为什么不把编辑放在模型外面？" | 作者的 MeLLo 就是外置记忆加迭代提问，能缓解，但不改模型本身 |
| 11 | Zhang 等，ICLR 2025 | 编辑会"过拟合"：只要问题里同时出现主语和关系，就冒出新答案。微软创始人的例子从 0.27% 升到 41% | | |
| 11 | Xie 等，ACL 2025 | 编辑是表面的：原来的知识还留在后面几层的注意力头里，而且有因果作用 | | |
| 10 下 | Yang 等，ACL 2025 | 在真实评测（WILD）下，编辑成功率从 96.8% 掉到 38.5%，原来的测试用了 teacher forcing 泄露了答案 | | |
| 10 下 | Hu 等，预印本 | 去学习后，用相关的维基文本微调一下，原文就逐字回来 | | |
| 10 下 | Hammoud 等，EMNLP Findings 2024 | 合并模型会把其中一个专家的不对齐也合进来 | | 注意：化学和数学专家只是论文图 1 的示意，不是实验 |
| 10 下 | Shrestha 等，2026 | 剪层再修复，分类能恢复到 90%，生成和算术恢复不了 | | |
| 11 下 | Arditi 等，NeurIPS 2024 | 13 个开源对话模型里，"拒绝"由一个方向控制，减掉它就不再拒绝 | "拒绝真的是一个方向，还是只是最容易找到的那个？" | 论文显示一个方向就够切换行为，但不排除还有别的表示 |
| 11 下 | Tan 等，NeurIPS 2024 | 同一个 steering 向量，在很多数据集上接近一半的输入往反方向走 | | 只测了两个对话模型 |
| 12 下 | Meng 等，ROME，NeurIPS 2022 | 因果追踪：先破坏输入，再逐个恢复内部状态，看哪里恢复了答案。事实在主语位置的中层 MLP 被查出来，再由后层注意力带到答案位置。编辑是对一个 MLP 做秩一更新 | | |
| 12 | Hase 等，NeurIPS 2023 | 事实"存在哪里"和"在哪里改有效"几乎无关（相关系数负 0.13），编辑成功的方差 94.7% 由选哪一层解释 | "因果追踪没用了？" | 用来选编辑层没用，用来理解存储仍然有用 |
| 12 | Guo 等，ICML 2025 | 改得稳的关键是对准"查表"机制，而不是泛泛地定位 | | |
| 17 | Gardner，Frames of Mind，1983 | 多元智能，七种（语言、逻辑数学、音乐、空间、身体动觉、人际、内省） | | |
| 17 | 李飞飞，From Words to Worlds，2025 年 11 月 Substack 长文 | 空间智能是 AI 的下一个前沿 | | Lenny's Podcast（2025 年 11 月）里她区分语言智能和空间智能，并说 AI 还缺情感智能 |
| 18 | Picard，Affective Computing，1997 | 让计算机能识别、表达，某些情况下"拥有"情感 | | |
| 18 | Minsky，The Emotion Machine，2006 | 情绪状态是开启一些资源、关掉另一些资源的结果 | | 页码待查 |
| 18 | Meyer，1956，第 31 页 | 当期待被暂时压住或彻底阻断时，情感就被唤起 | | |
| 18 | Salimpoor 等，Nature Neuroscience 2011 | 音乐快感高峰前尾状核释放多巴胺，高峰时伏隔核释放 | | |
| 18 下 | Hiller 和 Isaacson，1957 | Illiac Suite，第四个实验用马尔可夫链作曲 | | |
| 22 下 | McFee 和 Ellis，ISMIR 2014，Karystinaios 等 | 节拍为节点的自相似图能切出歌曲段落。GNN 找终止式和手工特征持平。Tonnetz 轨迹在作曲家分类上 0.49，风格分类上 0.84 | | |
| 23 下 | Copet 等，MusicGen，NeurIPS 2023 | 声音先被 EnCodec 切成每秒 50 帧、每帧 4 个码本的整数，再像 GPT 一样预测下一个 | | |
| 23 | Wei 等，ISMIR 2024 | 在 MusicGen 和 Jukebox 各层上训练线性探针，乐理概念（速度、音、和弦等）都能读出来。平均分把分类准确率和速度回归的 R² 混在一起 | "能读出来不代表模型在用。" | 对，所以第 24 页讲 steering，第 26 页讲因果检验 |
| 23 | Do Music Foundation Models Embed Pitch in Helical Structure?，arXiv 2607.29086，2026 年 7 月 | 把 C3 到 B5 共 36 个单音送进 Jukebox 和 MusicGen large，每层做 PCA 投到三维再拟合螺旋。两个模型都有螺旋，越深越清楚（Jukebox 平均 2.28，MusicGen 1.16，随机点 0.37）。形状随音色变：哈蒙德风琴每八度绕一圈，电吉他清音绕两圈 | "MusicGen 里的音高螺旋不是已经有人做了吗？" | 对，这条路被占了，我们不做音高几何。螺旋和五度圈是单个状态"在哪里"的几何，我们读的是状态之间"接下来去哪"的转移图 |
| 23 | Kanatas 等，What Makes a Good Layer?，ISMIR 2026 | 12 个音乐基础模型（含 MusicGen 小中大、MERT），看哪些无标签指标能挑出好层。调性任务上，只有他们新提的"移调等变性"有效：调性探针投到五度圈上，移调后相位按理论转动。调性任务在最深层最好 | "时间上的动态不是也有人量过吗？" | 他们有一个 temporal curvature（相邻帧位移向量的平均夹角），是轨迹的一个统计量，不是图。这是离我们最近的，被问到就这么答 |
| 25 下 | Schrimpf 等 PNAS 2021，Caucheteux 和 King 2022，Goldstein 等 2022，Kell 等 2018，Tuckute 等 2024 | 语言模型预测下一个词越准，越能预测大脑活动。大脑在词出现前就在预测。音频网络的中间层对应初级听觉皮层。模型挑出的句子能调高或调低语言网络的活动 | | |
| 25 | Pearce，IDyOM | 可变阶马尔可夫模型，多个"视角"，长期加短期记忆，给每个音一个信息量（意外程度） | "和你们的 12 节点图是什么关系？" | 同一类东西，它记得更长、看得更多 |
| 25 | Di Liberto 等，eLife 2020 | 20 人听巴赫单旋律，IDyOM 的意外程度在声学特征之外还能解释 EEG，20 人里 16 人显著，效应量 d 约 1.6，主要在音后 350 毫秒内，3 位病人的 ECoG 定位在听觉皮层附近 | | |
| 25 下 | Bellier 等，PLOS Biology 2023 | 29 位病人、2,668 个电极，从颅内信号重建 Pink Floyd 的歌，非线性解码 0.43 | | |
| 25 下 | Denk 等，Nature Communications 2025 | fMRI 到 MuLan 嵌入再到 MusicLM，能重建风格和乐器，速度重建不出来 | | |
| 26 下 | Noguchi 等，2026 | 用 MusicGen 的下一个 token 概率作为 EEG 解码器的教师信号，识别率 0.823 到 0.887 | | 用的是输出，不是内部 |
| 26 下 | Pepino 等，2025 | 36 个音频模型，任务表现越好，和 fMRI 越吻合 | | |

## 三、讲之前要补的三件事
1. 单向 steering 的评判器对照（第 24 页），需要投稿论文的数据。
2. Minsky 引文页码。
3. 李飞飞：查不到"五种智能"的原始出处，能查到的是 2025 年 11 月 Lenny's Podcast 里她明确讲了语言智能和空间智能，情感智能是"AI 还缺的能力"。卡片已改成这三项。

## 五、2026 年要知道的相近工作（第 6 轮文献检索，11 月 4 日）

按被问到的可能性排序。前三条已核对过原文，后两条来自检索代理，讲之前再自己看一眼。

1. Mischler、Mesgarani 等，Nature Communications，2025 年 10 月：用一个符号音乐生成模型（Musicautobot）的 13 层去拟合 EEG（10 位钢琴家，10 位非音乐人）和颅内记录，层越深预测越好，音乐人用的上下文更长。所以"大脑只从外部见过生成模型"不对了，第 26 页和它下面的 backup 已改成"见过输出、嵌入和层，但从没见过状态转移图"。
2. Narashiman 等，arXiv 2506.10225（2025 年 6 月，2026 年 5 月 v2）：用线性探针权重在 MusicGen 残差流上做风格 steering，已加到第 6 页引用。检索代理说 SMITIN 附录 D 也做了反方向（负强度），不对称性随乐器而变（吉他、钢琴好删难加，鼓和贝斯相反），这条没核对，讲之前看一下。所以第 6 页已改成"for the styles we tested"。
3. Circuit-Diff，Friedman 和 Song，arXiv 2609.23892，2026 年 9 月：在一次事实编辑前后比较 attribution graph，用来给特征贴标签。是 delta graph 最近的"表亲"，区别是我们给编辑排风险，他们定位知识。第 4 页标题已改成"applied as a vector"。
4. 编辑后内部痕迹的几篇（检索代理给出，未核对）：Suppressed, Not Erased（arXiv 2609.18985），The Anatomy of an Edit（arXiv 2603.20795），One Mask to Rule Them All（arXiv 2605.28839）。回答：它们查单个事实或解释机制，delta graph 给所有编辑打分排序，而且形状胜过单个数字。
5. Whyatt 和 Harrison，arXiv 2608.19061（未核对）：Essen 上音高特征决定分类，节奏贡献很小。被问到第 21 页时：任务不同（二分类，按地域），而且六个语料上音长的增益部分来自记谱方式，备注里已经写了。也可能有人说"这就是 Conklin 的 viewpoints"，承认是同一框架，我们的点是放在图的语言里。

## 六、英文答问稿（第 7 轮模拟提问，12 题）

现场要用英文答，所以答案直接写英文。每题后面标了答案现在在哪，以及哪里需要你确认。标"需要你"的地方，确认前不要说具体数字。

**Q1（统计）** "A partial correlation over 64 blocks from 12 prompts is singular. Isn't the graph mostly the ridge penalty?"
"You are right that 12 prompts cannot pin down that precision matrix, so we use ridge with one fixed lambda, the same estimator before and after, and we only use the difference. The evidence that the difference carries signal is held out: trained on 200 facts and tested on 500 new ones the AUC stays at 0.840 to 0.862, and rerunning the 50 riskiest edits flips only 2 of 50. A null with random probe prompts is the next control."
在哪：第 13 页备注，13 下 backup 第 4 步。需要你：SDM 附录里有没有随机 prompt 的对照。

**Q2（理论）** "ROME writes one layer, so the knot is just where the editor wrote. What is your null?"
"The prior already knows the editor and the model, so the gain from 0.703 to 0.797 is on top of knowing where the edit was written. Features are rank normalized within each model and editor pair, so an edit is only compared with edits by the same tool on the same model. Between two ROME edits, the shape of the change adds 0.093 AUC where the best single number adds 0.047."
在哪：13 下 backup 第 7 步，第 15 页。需要你：确认 Table F.1 的特征也做了这个归一化。

**Q3（敌意，NLP）** "Reading outputs gets 0.984, you get 0.797, and 7.4 minutes per fact is not cheap. Why use this?"
"Reading the outputs is the better judge, and we say so on the slide. Ours is triage: the costly generation and scoring then run only on the flagged 20 percent, about 5 times less follow up work. With a handful of edits, read the outputs. The method is for thousands of edits on a model that keeps changing."
在哪：第 16 页和备注。需要你：7.4 分钟包含哪些步骤，以及读输出这个基线每个编辑要多久。没有这个数字之前，不要说"更便宜"，只说"少做五倍的后续检查"。

**Q4（敌意，知识图谱）** "Only 1.3 percent lack a path, so the graph explains one point of a 60 point cliff."
"The graph's job is to split the cliff into two causes before any model runs. On MIMIC it says the record is not the problem, 3 of 239, so the remaining 50 to 70 points are the models' reasoning. On CORAL it goes the other way, 8.2 percent have no path and adding 51 edges takes that to zero."
在哪：第 9 页和备注（已加）。需要你：51 条边是人工加的还是模板自动加的。

**Q5（安全或系统）** "Can an editor game your scorer? Does it transfer from Qwen to Llama?"
"We have not tested an adversary who knows the scorer, and cross model transfer is also untested, our cross validation is grouped by fact within each model and editor pair. Those are the next two experiments: train on Qwen and test on Llama, and let an editor optimize against the scorer."
在哪：没有。需要你：探针 prompt 是否公开。

**Q6（看图仔细的 ML）** "A note plus length node has more cells, and your plus 3 points is inside the noise."
"Fair, so the honest comparison is within one node type. With pitch only, a second note of memory adds 8 points. With pitch plus length it adds nothing, 86.8 to 86.2, and that is the result I stand on. Differences of one to three points are inside the fold spread of about 2.7, so 73.3 against 70.2 is a tie. Counting pitch and length with no order already gives 68.4, so order still adds 18 points."
在哪：第 21 页备注。需要你：音长分了几类，以及 86.8、86.2、88.7 这几行的标准差。

**Q7（音乐信息学）** "This is Conklin and Witten's viewpoints and IDyOM. What is new?"
"Nothing on those slides is new as a model, it is viewpoints and IDyOM, and I show it because the rest of the talk needs that baseline: a first order graph that a listening brain measurably tracks. The new question is the plan: whether the same kind of transition graph exists inside a neural generator that was never given a note."
在哪：18 下 backup，第 25 页。

**Q8（懂音频 steering 的）** "SMITIN already reports negative strength steering and an asymmetry that flips by instrument."
"Our finding is for genre directions on the styles we tested, and I phrase it that way on purpose. If the asymmetry flips by instrument, that is what a reachability picture would predict: islands differ in how many ways in they have, and the plan is to measure that rather than assume it."
在哪：只有本备忘第五节。需要你：讲之前读一下 SMITIN 附录 D，确认它到底写了什么。

**Q9（敌意，HCI）** "Slide 24 has no numbers. How many styles, clips, which judge, is the judge biased?"
"The slide is a drawing of the result, the per clip numbers are in the paper under review." 接着说：需要你给一句可以公开的话（几种风格，每组多少段，用什么评判，一个效果大小，有没有用真实爵士和真实古典做评判器的对照）。这是现在最弱的一处。

**Q10（理论，计划）** "A fine enough clustering reproduces the generator's own surprisal. What is the null?"
"Matching the generator is a floor, not a proof. The test needs a null graph of the same size, for example shuffled transitions, and the real graph has to explain EEG beyond that null." 这是对计划的修改，要不要这样定由你决定。需要你：打算聚成多少类，为什么用中间层（第 23 页说调性在最深层最清楚）。

**Q11（做 EEG 的音乐老师）** "IDyOM needs notes, MusicGen makes audio at 50 steps a second. How do you align, and who records the EEG?"
"The first version uses pieces whose score we know, so IDyOM reads the score and the inside graph is read from MusicGen on the same material, with onsets from the score. It can start on public EEG music datasets before we record anything." 需要你：怎么让 MusicGen 演奏已知的谱，以及 EEG 的合作者、实验室和伦理审批。

**Q12（其实是评论，图挖掘）** "A partial correlation matrix is a graph only by courtesy. The title question cannot be false."
"If graph meant any matrix the title would be empty. The claim in Part 1 is that graph properties of the change carry information its size does not: 0.52 to 0.59 for single numbers against 0.798 with the shape. In Part 2 it is falsifiable: if the graph read from inside the generator explains the listener no better than the generator itself, it was our drawing, not the model's."
在哪：第 7、15、26 页。

## 四、时间预算（主线 27 页）

第 4 轮评审在上轮表格上逐页调整（按口头压缩后的讲法），再去掉下放的 4 页，主线约 36 分钟，加上四句过渡约 37 分钟，留 8 分钟左右给提问。排练后按实际改。

| 段落 | 页 | 秒数 | 累计 |
|---|---|---|---|
| 开场预告 | 1 到 7 | 45, 90, 75, 75, 90, 60, 45 | 8:00 |
| Part 1 语言 | 8 到 16 | 20, 120, 75, 90, 90, 150, 90, 75, 70 | 21:00 |
| Part 2 音乐 | 17 到 24 | 75, 75, 90, 75, 90, 135, 75, 60 | 32:15 |
| 大脑与收尾 | 25 到 27 | 90, 90, 45 | 36:00 |

口头压缩的要点：第 2 页三个问题一次出，第 3 页不念 86% 和 49%，第 4 页不在这里解释 AUC，第 5 页动画控制在 20 秒，第 6 页四种 steering 一口气说完，第 19 页两段音乐各放 8 秒左右。

backup 页（按向下键）：9 下四类失败，10 下七种手术和四个证据，11 下"向量在单个输入上失败"（Arditi 和 Tan），12 下 Meng 的因果追踪图，13 下方法八步，16 下完整四个局限，18 下最早的音乐模型（1957 年的马尔可夫作曲和 IDyOM），21 下记忆长度那张图（这张的 LLM 评判数字来自网站上的旧实验），22 下"何时图有用"综述，23 下 MusicGen 是什么，25 下语言模型预测大脑和 Brain2Music，26 下"只从外部相遇"的三篇工作。

最可能被追问的一题："delta graph 是真的，还是 12 个探针 prompt 造出来的？"答三点：探针 prompt 和定义失败的 prompt 不重叠，用 200 个事实训练、500 个新事实测试，AUC 仍有 0.840 到 0.862，把风险最高的 50 个编辑从头重跑，只有 2 个翻转。
