from config import config
from app.models import UserCaptcha, CaptchaStatus, CaptchaLang


dev_config = config.get("development")
session = dev_config.Session(bind=dev_config.engine)


class CaptchaController:
    def new_user_captcha(self, user_id):
        new_user = UserCaptcha(user_id=user_id)
        session.add(new_user)
        session.commit()

    def delete_user_captcha(self, user_id):
        user = session.query(UserCaptcha).filter_by(user_id=user_id).first()
        session.delete(user)
        session.commit()

    def get_user(self, user_id):
        return session.query(UserCaptcha).filter_by(user_id=user_id).first()

    def get_group_params(self, group_id):
        return (
            session.query(CaptchaStatus).filter_by(group_id=group_id).first(),
            session.query(CaptchaLang).filter_by(group_id=group_id).first()
        )

    def set_status(self, status, group_id):
        captcha_group = self.get_group_params(group_id)[0]
        captcha_group.status = status
        session.commit()

    def set_default_settings(self, group_id):
        df_status = CaptchaStatus(
            group_id=group_id,
            status="on"
        )

        df_lang = CaptchaLang(
            group_id=group_id,
            lang="en"
        )
        
        session.add(df_status)
        session.add(df_lang)
        session.commit()

    def set_lang(self, lang, group_id):
        captcha_group = self.get_group_params(group_id)[1]
        captcha_group.lang = lang
        session.commit()

    def select_status(self, group_id):
        return self.get_group_params(group_id)[0].status

    def select_lang(self, group_id):
        return self.get_group_params(group_id)[1].lang