# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

# 游戏在此开始。

label start:

    $ name = 'Shawn' #user input
    define e = Character('[name]')

    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为“bg room.png”或“bg room.jpg”）来显示。

    scene bg room

    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # “eileen happy.png”的文件来将其替换掉。

    show eileen happy

    # 此处显示各行对话。

    "Welcom to Chinese{b}Daily{/b}!"

    $day=1
    $correct=0
    $wrong=0

    'Day [day]'

    """Today\'s vocabulary: (Please memorize)\n
        早上(zao3shang4)  morning; in the morning\n
        中午(zhong1wu3) noon; at noon\n
        晚上(wan3shang4)  night; at night\n
        早饭(zao3fan4)  breakfast\n
        午饭(wu3fan4)   lunch\n
        晚饭(wan3fan4)  dinner\n
        吃(chi1) eat"""

    e 'I {b}eat{/b} three meals per day:'

    menu:
        '吃(chi1)':
            'Correct!'

    e 'I eat three meals per day:\n{b}Breakfast{/b}'

    menu:
        '早上(zao3shang4)':
            $wrong+=1
            'This is not correct'
        '早饭(zao3fan4)':
            $correct+=1
            'Correct!'
        '晚饭(wan3fan4)':
            $wrong+=1
            'This is not correct'

    e 'I eat three meals per day:\n早饭(zao3fan4) {b}in the morning{/b}'

    menu:
        '早上(zao3shang4)':
            $correct+=1
            'Correct!'
        '早饭(zao3fan4)':
            $wrong+=1
            'This is not correct'
        '晚上(wan3shang4)':
            $wrong+=1
            'This is not correct'

    e """I eat three meals per day:\n
        早上(zao3shang4)吃(chi1)早饭(zao3fan4)\n
        {b}lunch{/b}"""

    menu:
        '午饭(wu3fan4)':
            $correct+=1
            'Correct!'
        '早饭(zao3fan4)':
            $wrong+=1
            'This is not correct'
        '中午(zhong1wu3)':
            $wrong+=1
            'This is not correct'

    e """I eat three meals per day:\n
        早上(zao3shang4)吃(chi1)早饭(zao3fan4)\n
        午饭(wu3fan4) {b}at noon{/b}"""

    menu:
        '午饭(wu3fan4)':
            $wrong+=1
            'This is not correct'
        '早饭(zao3fan4)':
            $wrong+=1
            'This is not correct'
        '中午(zhong1wu3)':
            $correct+=1
            'Correct!'

    e """I eat three meals per day:\n
        早上(zao3shang4)吃(chi1)早饭(zao3fan4)\n
        中午(zhong1wu3)吃(chi1)午饭(wu3fan4)\n
        {b}dinner{/b}"""

    menu:
        '午饭(wu3fan4)':
            $wrong+=1
            'This is not correct'
        '早饭(zao3fan4)':
            $wrong+=1
            'This is not correct'
        '晚饭(wan3fan4)':
            $correct+=1
            'Correct!'

    e """I eat three meals per day:\n
        早上(zao3shang4)吃(chi1)早饭(zao3fan4)\n
        中午(zhong1wu3)吃(chi1)午饭(wu3fan4)\n
        晚饭(wan3fan4) {b}at night{/b}"""

    menu:
        '晚上(wan3shang4)':
            $correct+=1
            'Correct!'
        '午饭(wu3fan4)':
            $wrong+=1
            'This is not correct'
        '晚饭(wan3fan4)':
            $wrong+=1
            'This is not correct'

    e """I eat three meals per day:\n
        早上(zao3shang4)吃(chi1)早饭(zao3fan4)\n
        中午(zhong1wu3)吃(chi1)午饭(wu3fan4)\n
        晚上(wan3shang4)吃(chi1)晚饭(wan3fan4)"""

    $score=correct/(correct+wrong)
    if score < .8:
        'Sorry, you did not pass today\'s lesson, 80\% correct is required.'
        jump start
    else:
        'Congratulations! You have finished lesson of Day1.'
        """You have learned:\n
        早上(zao3shang4)  morning; in the morning\n
        中午(zhong1wu3) noon; at noon\n
        晚上(wan3shang4)  night; at night\n
        早饭(zao3fan4)  breakfast\n
        午饭(wu3fan4)   lunch\n
        晚饭(wan3fan4)  dinner\n
        吃(chi1) eat"""

        'Your Chinese learning has officially started!'
        'You can choose topic(s) you want to learn per day. A score >80\% is required to pass each topic.'
        'We recommend you to learn one day of topic per day for better learning outcomes.'
        jump daily

label daily:
    $day+=1
    'Day [day]'

    # 此处为游戏结尾。

    return
