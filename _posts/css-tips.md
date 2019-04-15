# css语法结构
## css属性与选择符
css语法有三个部分组成：选择符（selector），属性（Property）和值（Value）。
- 标签组选择符
```css
body {background-color:blue;}
p{
    text-align: center;
    color: black;
    font-family: arial;
} ```
- 选择符还支持同时选择群组
```css
h1,h2,h3,p,span{
    font-size: 12px;
    font-family: arial;
} ```
css包含选择符：
```css
h1 span{
    font-weight: bold;
}```
表示h1标签下的span标签
- id 选择符
> 在网页中每个 id 只能使用一次。
```html
<div id="content"></div>
```
相应的 css 为
```css
#content {
    line-height: 130%;
}```
- class 选择符
> class 选择符允许标签重复使用。
```html
<div class="clz1"></div>
<h1 class="clz1"></h1>
<h3 class="clz1"></h3>
```
根据 class 来对所有使用了这个 class 的标签进行样式绑定。
```css
.clz1{
    color: red;
}
```
- 标签指定式选择符
```css
h1 #content {
    color: red;
}```
> 该样式会作用于所有 h1 标签下的 id 为 content 的元素。
- 伪类及伪对象
伪类及伪对象是一种特殊的类和对象，它由 css 自动支持，属 css 的一种扩展型类和对象。
伪类及伪对象的名称不能被用户自定义，使用时只能按照标准格式进行应用。
```css
div:hover{
    background-color: blue;
}```
> 本例中 hover 就是一个伪类。 css 内置了几个标准的伪类，可用于样式的定义。
几个标准伪类：
1. :link         a链接标签的未被访问样式
2. :visited      a链接标签的访问后样式
3. :hover        鼠标移动到对象上时的样式
4. :active       鼠标在对象上按下时的样式
5. :focus        对象成为输入焦点的样式
6. :first-child  对象的
7. :first
