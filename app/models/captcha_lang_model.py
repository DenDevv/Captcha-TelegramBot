from sqlalchemy import Column, BigInteger, Integer, String

from config import config


dev_config = config.get("development")


class CaptchaLang(dev_config.Base):
    __tablename__ = "captcha_lang"
    id = Column(Integer(), primary_key=True)
    group_id = Column(BigInteger(), nullable=False)
    lang = Column(String(2), nullable=False)