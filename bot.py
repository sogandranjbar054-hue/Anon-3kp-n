import os
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")

ADMIN_IDS = {
    5331612290,
    6789331178,
    5547081583,
    5249995613,
}

async def receive_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return

    user = update.effective_user

    # پیام را بدون نام، یوزرنیم یا آیدی فرستنده برای ادمین‌ها می‌فرستیم
    text = update.message.text

    if not text:
        await update.message.reply_text("فعلاً فقط پیام متنی قابل ارسال است.")
        return

    anonymous_text = (
        "📩 پیام ناشناس جدید\n\n"
        f"{text}"
    )

    for admin_id in ADMIN_IDS:
        try:
            await context.bot.send_message(
                chat_id=admin_id,
                text=anonymous_text
            )
        except Exception as e:
            print(f"Could not send to {admin_id}: {e}")

    await update.message.reply_text(
        "✅ پیامت با موفقیت به‌صورت ناشناس ارسال شد."
    )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            receive_message
        )
    )

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
