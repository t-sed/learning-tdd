
[![github-pytest](https://github.com/t-sed/learning-tdd/workflows/tdd/badge.svg)](https://github.com/t-sed/learning-tdd/actions?query=workflow%3Atdd)

---
marp: true
---

# Pythonで学ぶTDD

---

# アジェンダ
* TDDとは
* TDD開発の流れ
* TDDがもたらす影響
* プログラミングの流れ
* 使用するフレームワーク、pytestについて
* サンプルプロジェクト
* 開発要件1：レッド
* 開発要件1：グリーン
* 開発要件1：リファクタリング
* TDDの批評
* TDDが運用されたことで解決した問題
* 総括
* 参考リンク集

---

# TDDとは
「動作する綺麗なコード」をゴールとした考え方です。

---

# 開発の流れ
1. テストリストを作成する
2. 新たなテストコードを書く
3. 自動化されたテストが失敗した時のみ、新しいコードを書く
4. 重複を削除する

---

# TDDがもたらす影響
* 有機的な設計
* テストを高頻度で回すために、迅速に応答する開発環境が構築される
* 凝集度が高く、結合度の低い部品で構成された設計になりやすい

---

# TDDのプログラミングの流れ
1. レッド：動作しない、コンパイルすら通らないテストを書く
2. グリーン：テストを迅速に動作させる。罪深いことをしても良い
3. リファクタリング：テストを通すために重複を全て削除する

---

# pytestについて
pytestは、小さなテストだけでなく、アプリケーションやライブラリの複雑な機能テストの作成をサポートするライブラリです。
https://docs.pytest.org/en/stable/

---
# pytestのコード例

```python
def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 5
```

---

# サンプルプロジェクト
あなたは多国通貨のレポートを出力するアプリ開発を担当するエンジニアです。
下記要件の開発を担当しました。
1. 単一通貨に対してかけ算ができる
2. 2つの通貨の足し算ができる(TBA)
[サンプルリポジトリ](https://github.com/t-sed/learning-tdd)

---
# 開発要件1：レッド
単一通貨に対して掛け算するためのテストコードを書く。
```python
# tests/test_doller.py
from src.money import Dollar

def test_times():
    five_dollar: Dollar = Dollar(5)
    five_dollar.times(2)
    assert five_dollar.amount == 10

if __name__ == '__main__':
    test_times()
```

---
# 開発要件1：グリーン
テストコードを通すために、main.moneyを書く。テストを通すために悪魔の実装をする。
```python
# main/money.py
class Dollar:
    def __init__(self, amount: int):
        # テストを通すための悪魔の実装
        self.amount = 10

    def times(self, times: int):
        pass

```
---
# 開発要件1：リファクタリング工程①

```python
# main/money.py
class Dollar:
    def __init__(self, amount: int):
        self.amount = amount

    def times(self, times: int):
        # テストを通すための悪魔の実装
        self.amount = 5 * 2

```

---
# 開発要件1：リファクタリング工程②

```python
# main/money.py
class Dollar:
    def __init__(self, amount: int):
        self.amount = amount

    def times(self, times: int):
        # テストを通すための悪魔の実装
        self.amount *= times

```

---

# TDDの批評
TDDはあくまで「動作する綺麗なコード」を書くことに焦点を向けたプラクティスであるため、銀の弾丸ではないです。
特に、TDDのプラクティス上、ユニットテストが多くなる、テストしやすい単位に細分化、間接化されるため、アーキテクチャが複雑になる、結合テストが軽視されやすくなるといったデメリットが挙げられます。
https://twop.agile.esm.co.jp/what-practice-should-be-remain-if-you-stop-tdd-239071f7102e

---

# TDDが運用されたことで解決した問題
これに対して、TDDを考案した方はTDDの布教によって解決された問題は以下だと、facebookで発言しております。
* 過剰性能（Over-engineering）
* インタフェースと実装の分離
* ドキュメンテーション
* APIフィードバック
* 論理エラー
* 大きな問題
* プログラマ同士の問題共有
* プログラムが期待通りに動作している事を確認
https://www.facebook.com/notes/kent-beck/rip-tdd/750840194948847

---

# 総括
* TDDは「動作する綺麗なコード」を書くことに焦点を向けたプラクティス
* レッド→グリーン→リファクタリングの流れ

# 所感
* TDDのメリットデメリットは色々議論されているため、調べると面白かったです
* 色々なプラクティスを試した上で、プロジェクトや自分に合った開発プラクティスを考えて提唱していけたら、エンジニアとしてのレベルも高まるのかなと思いました

---

# 参考リンク集
* [testing vs checking](https://www.developsense.com/blog/2009/08/testing-vs-checking/)
* [testing and checking refined](https://www.satisfice.com/blog/archives/856)
* [doctestの公式リンク](https://docs.python.org/ja/3/library/doctest.html)
* [doctestとpytest等の使い分け](https://stackoverflow.com/questions/361675/python-doctest-vs-unittest)
* [pytestの紹介記事](https://www.m3tech.blog/entry/pytest-summary#%E3%83%86%E3%82%B9%E3%83%88%E3%82%92%E6%9B%B8%E3%81%8F)
* [TDDの批判まとめ](https://twop.agile.esm.co.jp/what-practice-should-be-remain-if-you-stop-tdd-239071f7102e)
* [TDD is dead. Long live testing.](https://yattom.hatenablog.com/entries/2014/04/24)

---

# おまけ：doctestについて
doctestとは、対話的 Python セッションのように見えるテキストを探し出し、セッションの内容を実行して、そこに書かれている通りに振舞うかを調べるモジュールです。

---
# doctestのコード例

```python
def factorial(n:int):
    """Return the factorial of n, an exact integer >= 0.
    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0
    """

    import math
    if not n >= 0:
        raise ValueError("n must be >= 0")
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
```
