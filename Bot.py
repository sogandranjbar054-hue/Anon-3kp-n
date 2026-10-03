import os
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("8933371442:AAG3VBCeksA5tBo-rsn7FYMDLZRRIzKmBFE")

ADMIN_IDS = {
    @Cryin0g,
    @Ansel1387,
    @Elina_dla,
    @iilwel,
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
