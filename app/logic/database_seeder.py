import json

from app.abstractions.transaction_manager import ITransactionManager


class DatabaseSeeder:
    def __init__(self, data_path: str, transaction_manager: ITransactionManager):
        self.data_path = data_path
        self.transaction_manager = transaction_manager

    async def fill_database(self) -> None:
        await self.__clear_database()

        with open(self.data_path, mode="r", encoding="UTF-8") as data_file:
            celebrity_data = json.load(data_file)

        for celebrity in celebrity_data:
            await self.__parse_celebrity(celebrity)

        await self.transaction_manager.commit()

    async def __clear_database(self) -> None:
        await self.transaction_manager.celebrities.clear_database()

    async def __parse_celebrity(self, celebrity: dict) -> None:
        celebrity_data = celebrity.get("celebrity")
        daily_schedule_data = celebrity.get("daily_schedule")
        await self.transaction_manager.celebrities.insert_celebrity_data(
            **celebrity_data
        )
        await self.transaction_manager.celebrities.insert_daily_schedule_data(
            **daily_schedule_data
        )
