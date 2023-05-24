from aligned.worker import StreamWorker
from aligned import RedisConfig, FileSource

store = FileSource.json_at("https://raw.githubusercontent.com/MatsMoll/aligned-example/main/feature-store.json")

worker = StreamWorker.from_reference(
    store,
    RedisConfig.localhost()
).metrics_port(8000)