import warnings
warnings.simplefilter("ignore", DeprecationWarning)

import sys
from pathlib import Path
import asyncio

root = str(Path(__file__).resolve().parents[1])
sys.path.append(root)

from src.logger import logger
from src.config import config
from src.models import model_manager
from src.agent import create_agent
from src.utils import assemble_project_path

async def main():
    # Init config and logger
    config.init_config(config_path=assemble_project_path("configs/config_example.toml"))
    logger.init_logger(config.log_path)
    logger.info(f"Initializing logger: {config.log_path}")
    logger.info(f"Load config: {config}")

    # Registed models
    model_manager.init_models(use_local_proxy=False)
    logger.info("Registed models: %s", ", ".join(model_manager.registed_models.keys()))
    
    # Create agent
    agent = await create_agent()

    # Run example
    # task = "Use deep_researcher_agent to search the latest papers on the topic of 'AI Agent' and then summarize it."
    # task = "使用deep_researcher_agent搜索近期江苏足球联赛的新闻，简单总结一下火热的原因。"
    task = "使用deep_researcher_agent搜索近期上海螺纹钢价格相关内容，并简单做出分析报告。"
    res = await agent.run(task)
    logger.info(f"Result: {res}")

if __name__ == '__main__':
    asyncio.run(main())