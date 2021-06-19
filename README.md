# Problem Set .pdf file for FJCU Programming Exam or Contest
* 提供給輔大程式競賽上機考或比賽使用。
* 交大謝旻錚教授整理製作並授權使用。

# 新增題目資料夾
```
sh folder_generate.sh {folder_name}
```

# 生成測資
在資料夾內必須有 `AC.cpp` 和 `generate.sh`。

生成測資程式參考：https://github.com/luogu-dev/cyaron。

```
sh testdata_generate.sh {folder_name}
```

# 新增圖片模板
請將圖片放到 `image` 資料夾內。

```
\includegraphics[width=2in]{image/picture_name} \\
```