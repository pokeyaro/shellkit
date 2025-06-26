"""
docs/texts/reminder.py

Provides localized wellness reminder messages for the shell,
categorized by language and urgency level.
"""

from shellkit.i18n import I18N_EN, I18N_JA, I18N_KO, I18N_ZH

INFO_NORMAL = "normal"
INFO_CRITICAL = "critical"


REMINDER_TEXTS = {
    I18N_EN: {
        INFO_NORMAL: [
          "Remember to drink water and stretch 💧",
          "Don't forget to move your body after long work 🧘",
          "Close your eyes and relax for 10 seconds 💤",
          "Is your posture okay? Take a deep breath 🫁",
          "Hydrate yourself, or the bugs will multiply 🐞",
          "Step away from the keyboard, let your brain buffer 🧠",
          "You've worked hard—rest is not procrastination 🌿",
          "Take a mental break—maybe inspiration is waiting 🚪"
        ],
        INFO_CRITICAL: [
          "You've been working for {time}. Time to walk around 🚶💥",
          "It's been {time}. Rest now—don't trade your health for passion 🔥💥",
          "{time} of work—your keyboard is getting tired too ⌨️💥",
          "{time} has passed. You deserve a proper mental reset 🧘💥",
          "Bro, it's been {time}! Even your chair wants you to stretch 🪑💥",
          "You've been coding for {time}. Time to reboot your brain 🔄💥",
          "Workaholic alert! {time} without rest—bugs will strike back 🚨💥",
          "{time} marathon done. Time to refuel 🏃‍♂️💥"
        ]
    },
    I18N_JA: {
        INFO_NORMAL: [
          "お水を飲んで、少しストレッチしましょう 💧",
          "長時間の作業の後は体を動かしてね 🧘",
          "10 秒間、目を閉じてリラックス 💤",
          "姿勢は大丈夫？深呼吸してみて 🫁",
          "水分をとって、バグを防ぎましょう 🐞",
          "キーボードから少し離れて、脳を休めよう 🧠",
          "よく頑張ってるよ。休むのはサボりじゃない 🌿",
          "ちょっとぼーっとしてみて。ひらめきが待ってるかも 🚪"
        ],
        INFO_CRITICAL: [
          "{time} 作業しました。少し歩きましょう 🚶💥",
          "{time} 頑張ったね。休憩しよう！健康を大切に 🔥💥",
          "{time} も作業中。キーボードも疲れてるよ ⌨️💥",
          "{time} が経ちました。しっかり休んで 🧘💥",
          "もう {time}！椅子が立ち上がって欲しがってるよ 🪑💥",
          "{time} コーディング中。脳を再起動しましょう 🔄💥",
          "働きすぎ警報！{time} 休まず…バグが襲ってくるよ 🚨💥",
          "{time} のマラソン終了！エネルギー補給しよう 🏃‍♂️💥"
        ]
    },
    I18N_KO: {
        INFO_NORMAL: [
          "물 좀 마시고 스트레칭하는 거 잊지 마 💧",
          "오래 일했으니까 몸 좀 움직여 🧘",
          "눈 감고 10초간 쉬어 💤",
          "자세 괜찮아? 심호흡 한 번 해봐 🫁",
          "물 마셔, 안 그러면 버그가 늘어날 거야 🐞",
          "키보드에서 좀 떨어져서 뇌 버퍼링 시켜 🧠",
          "열심히 했어—쉬는 게 게으른 게 아니야 🌿",
          "정신적으로 좀 쉬어—영감이 기다리고 있을지도 🚪"
        ],
        INFO_CRITICAL: [
          "{time} 동안 일했어. 이제 좀 걸어다녀 🚶💥",
          "{time} 지났어. 지금 쉬어—건강을 열정과 바꾸지 마 🔥💥",
          "{time} 일했네—키보드도 지쳤을 거야 ⌨️💥",
          "{time} 흘렀어. 제대로 된 정신적 리셋이 필요해 🧘💥",
          "야, {time}이야! 의자도 네가 스트레칭하길 원해 🪑💥",
          "{time} 코딩했어. 뇌를 재부팅할 시간이야 🔄💥",
          "일중독자 경보! {time} 쉬지 않으면 버그가 복수할 거야 🚨💥",
          "{time} 마라톤 끝! 연료 보충할 시간 🏃‍♂️💥"
        ]
    },
    I18N_ZH: {
        INFO_NORMAL: [
            "记得喝点水、伸个懒腰 💧",
            "工作久了别忘活动筋骨 🧘",
            "闭上眼睛放松 10 秒吧 💤",
            "坐姿还好吗？来个深呼吸 🫁",
            "喝点水，不然 bug 会变多 🐞",
            "离键盘远一点，让大脑补个帧 🧠",
            "你已经很努力了，休息不是拖延 🌿",
            "放空一下，灵感说不定正等你 🚪"
        ],
        INFO_CRITICAL: [
            "你已经持续工作 {time} 了，该起来走一走了 🚶💥",
            "工作 {time} 了，休息！别让身体为你的热爱埋单 🔥💥",
            "已经 {time} 了，再不起来动动，你的键盘都快替你累了 ⌨️💥",
            "{time} 已过，你值得一场好好地放空 🧘💥",
            "老兄，{time} 了！你的椅子都想让你起来透透气 🪑💥",
            "码了 {time}，大脑需要重启一下了 🔄💥",
            "工作狂警报！{time} 不休息，bug 会报复的 🚨💥",
            "{time} 马拉松选手，该补给一下了 🏃‍♂️💥"
        ]
    },
}
