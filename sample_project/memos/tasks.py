from celery import shared_task
from .models import Memo, AIComment
from time import sleep
from datetime import datetime

@shared_task
def create_ai_comment(memo_id):
    memo = Memo.objects.get(id=memo_id)

    # AI のコメントを生成する処理
    start_time = datetime.now().strftime("%H:%M:%S")
    sleep(3)
    end_time = datetime.now().strftime("%H:%M:%S")
    ai_comment = f"AI がコメントしました！ 処理は {start_time} <--> {end_time} 間に行われました。"
    
    # AI のコメントを保存する処理
    AIComment.objects.create(memo=memo, content=ai_comment)
    return
