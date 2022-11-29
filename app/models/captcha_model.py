from sqlalchemy import Column, BigInteger, Integer

from config import config


dev_config = config.get("development")


class UserCaptcha(dev_config.Base):
    __tablename__ = "captcha"
    id = Column(Integer(), primary_key=True)
    user_id = Column(BigInteger(), nullable=False)