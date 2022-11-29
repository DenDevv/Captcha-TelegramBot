from sqlalchemy import Column, String, Integer, BigInteger

from config import config


dev_config = config.get("development")


class CaptchaStatus(dev_config.Base):
    __tablename__ = "captcha_status"
    id = Column(Integer(), primary_key=True)
    group_id = Column(BigInteger(), nullable=False)
    status = Column(String(3), nullable=False)