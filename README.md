# ver 1.0 2023-03-31版

## 概要
urlを指定するとページから電話番号を取得してリストとして返す。

## 背景
クラウドソーシングサイトでクライアントが指定したURL(企業のURL)から電話番号を取得し、  
指定されたフォームやExcelにまとめる案件を目にした。  
人力だと時給500円にも満たない案件ばかりだが、この工程を自動化すれば、  
ミスなく素早く電話番号を取得出来ると考えた

## 今後の実装予定
Pandasを使ってExcelファイルから一括でURLを読み込み電話番号を一括でExcelに出力できるようにする -> ver 1.1
フレームワークを使ってWebアプリとして実装する　-> ver 1.2