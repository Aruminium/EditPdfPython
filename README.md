## clean機構 (--no-cache)
最後に不要なパッケージマネージャーのキャッシュを削除して容量を削減

```Dockerfile
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/*
```