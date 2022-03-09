# python 3.6 をベースにDockerイメージを作成
FROM python:3.6

# 作業ディレクトリを指定
WORKDIR /app

# カレントディレクトリのファイルをDockerコンテナの｢/app｣ ディレクトリにコピー
ADD . /app

# Flaskをインストール
RUN pip install Flask

# コンテナの実行コマンドを指定
CMD ["python", "app.py"]