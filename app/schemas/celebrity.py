from pydantic import UUID4, BaseModel, ConfigDict


class CelebritySchema(BaseModel):
    id: UUID4
    name: str
    age: int
    occupation: str
    short_bio: str


class CelebrityResponseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    celebrities: list[CelebritySchema]


class ScheduleSchema(BaseModel):
    activity_name: str
    start_time: str
    end_time: str


class DailyScheduleResponseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID4
    celebrity_id: UUID4
    schedule: list[ScheduleSchema]
