# 猿人学web逆向攻防大赛1-20题

这是我个人对猿人学web逆向赛1-20题的解题项目开源工程。

项目尽量提供还原协议的算法，不使用rpc等远程调用方式。例如github上对于第11题的答案，很多都是frida的方案，对于第7题则用的是图像识别的方案。为了减少项目中的依赖，提高逆向水平，我们在此采用了纯python版本还原算法的方案


## 解题完成度

以下表格显示了已完成的题目和待完成的题目。

| 编号 | 题目名                | 难度    | 分类    | 完成情况  |
|----|--------------------|-------|-------|-------|
| 20 | 新年挑战               | ★★★☆☆ | 骚操作   |  ☑   |
| 1  | js 混淆 - 源码乱码       | ★★☆☆☆ | js加密  | ☑     |
| 2  | js 混淆 - 动态cookie 1 | ★★★☆☆ | js加密  | ☑     |
| 3  | 访问逻辑 - 推心置腹        | ★★☆☆☆ | 骚操作   | ☑     |
| 4  | 雪碧图、样式干扰           | ★★☆☆☆ | css加密 | ☑     |
| 5  | js 混淆 - 乱码增强       | ★★★☆☆ | js加密  | ☑     |
| 6  | js 混淆 - 回溯         | ★★★☆☆ | js加密  |  ☑  |
| 7  | 动态字体，随风漂移          | ★★★☆☆ | css加密 |  ☑   |
| 8  | 验证码 - 图文点选         | ★★★★☆ | 验证码   |   ☑   |
| 9  | js 混淆 - 动态cookie 2 | ★★★★☆ | js加密  |     |
| 10 | js 混淆 - 重放攻击对抗     | ★★★★★ | js加密  |     |
| 11 | app抓取 - so文件协议破解   | ★★★☆☆ | 安卓    |  ☑ 纯算法版   |
| 12 | 入门级js              | ★☆☆☆☆ | js加密  | ☑     |
| 13 | 入门级cookie          | ★☆☆☆☆ | js加密  | ☑     |
| 14 | 备而后动-勿使有变          | ★★★★☆ | js加密  |    |
| 15 | 备周则意怠-常见则不疑        | ★★☆☆☆ | 骚操作   | ☑     |
| 16 | js逆向 - window蜜罐    | ★★☆☆☆ | js加密  | ☑     |
| 17 | 天杀的Http2.0         | ★☆☆☆☆ | 骚操作   | ☑     |
| 18 | jsvmp - 洞察先机       | ★★★★☆ | js加密  |     |
| 18 | 乌拉乌拉乌拉      | ★★☆☆☆ | js加密  | ☑     |