# Contest Tool

## Requirement
- docker-compose

## Build Environment
```
git clone https://github.com/marmot0814/Contest-Tool.git
cd Contest-Tool

make build
```

## Example
```
cp template/problem.tex.contest problem.tex
make pdf
```

## Add a problem
```
python script/folderGenerator.py test
```

## Acknowledge
* [FjuOnlineJudge/Contest-Tool](https://github.com/FjuOnlineJudge/Contest-Tool) 輔大開發 Contest-Tool
* 交大謝旻錚教授整理製作並授權使用。

## Reference
* 詳細教學：https://fjuonlinejudge.github.io/Training/tool/contesttool/
