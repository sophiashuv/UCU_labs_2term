import game

print("Гравець хоче побудувати університет на вулиці Козельницькій, але для цього йому потрібно перемогти злого Магната, "
      "що планує побудувати там казино, і також перемогти щонайменше 3 ворогів, які трапляться на його шляху.")
print("-" * 100)
print("Ось перелік команд:" + "\n" + "північ" + "\n" + "південь" + "\n" + "захід" + "\n" + "схід" + "\n" + "взяти" +
      "\n" + "боротись" + "\n" + "говорити" + "\n" + "почати")
print("-" * 100)
print("Напиши 'почати', якщо хочеш продовжити гру.")
kozelnytska = game.Street("Вул. Козельницька")
kozelnytska.set_description("Оооо, ця територія дуже гарна. Тут я хочу побудувати нові корпуси, для того, щоб відновити "
                            "діяльність заснованої Андреєм Шептицьким Української богословської Академії.")

stryiska = game.Street("Вул Стрийська")
stryiska.set_description("Як добре що я знаю короткий маршрут від вулиці Козильницької до Стрийської. Таким чином я "
                         "дістанусь до податкової адміністрації швидше за посіпак магната.")

franka = game.Street("Вул. І. Франка")
franka.set_description("На моєму шляху вулиця І.Франка. Хитрі посіпаки магната перекрили мій подальший маршрут, "
                       "як добре, що на цій вулиці є відділ міліції. Сподіваюсь, місцеві міліціонери захистять "
                       "невинного.")

saksahanskoho = game.Street("Вул. Саксаганського")
saksahanskoho.set_description("Тут живе моя бабця. Не можу не заглянути до неї в гості")

shevchenka = game.Street("Пр. Шевченка")
shevchenka.set_description("Оооо, ми уже на проспекті Шевченка. Якщо зайти у Шкоцьку кав'ярню обов'яково "
                           "зустрінемо мого товариша Нестора-математика.")


zelena = game.Street("Вул. Зелена")
zelena.set_description("Дорогу нам перегородив посіпака-філософ.")

kniazia_romana = game.Street("Вул Князя Романа")
kniazia_romana.set_description("Мої товариші з факультету архітектури Львівської політехніка розробили проект "
                               "будівництва корпусів мого університету.")

halytska = game.Street("Вул. Галицька")
halytska.set_description("Тут розташована мерія. Необхідно віддати довідку про доходи злій секретарці Галині.")

krakivska = game.Street("Вул. Краківська")
krakivska.set_description("Тут знаходиться бюро розподілу Державної землі")


stryiska.link_street(kozelnytska, "північ")
kozelnytska.link_street(stryiska, "південь")
franka.link_street(kozelnytska, "південь")
kozelnytska.link_street(franka, "північ")
franka.link_street(zelena, "північ")
zelena.link_street(franka, "південь")
saksahanskoho.link_street(franka, "схід")
franka.link_street(saksahanskoho, "захід")
saksahanskoho.link_street(shevchenka, "північ")
shevchenka.link_street(saksahanskoho, "південь")
shevchenka.link_street(halytska, "схід")
halytska.link_street(shevchenka, "захід")
halytska.link_street(krakivska, "північ")
krakivska.link_street(halytska, "південь")
zelena.link_street(kniazia_romana, "північ")
kniazia_romana.link_street(zelena, "південь")
kniazia_romana.link_street(halytska, "північ")
halytska.link_street(kniazia_romana, "південь")


curse_work = game.Enemy("Магнат", "Злий багатій, який планує побудувати казино замість мого університету.")
curse_work.set_conversation("Ха-ха-ха, я отримаю дохвіл швидше.")
curse_work.set_weakness("дозвіл")
kozelnytska.set_character(curse_work)

posipaka_b = game.Enemy("Посіпаки-батяри", "Кілька хлопців спортивної зовнішності найнятих магнатом, "
                        "аби протидіяти мені.")

posipaka_b.set_conversation("Ти нас не переможеш власноруч!!!")
posipaka_b.set_weakness("поліцейський")
franka.set_character(posipaka_b)

posipaka_l = game.Enemy("Посіпака-лотер", "Ще один прихвостень магната.")
posipaka_l.set_conversation("Я непереможний")
posipaka_l.set_weakness("ціпок")
shevchenka.set_character(posipaka_l)

posipaka_f = game.Enemy("Посіпака-філософ", "Ще один прихвостень магната. Любить поспілкуватися з розумними людьми.")
posipaka_f.set_conversation("Вам мене не заговорити")
posipaka_f.set_weakness("математик")
zelena.set_character(posipaka_f)

secretary = game.Enemy("Секретарка", "Пло суті жінка добра, але у всьому слідє букві закону. Правильно "
                       "виконана процедура вирішує все.")

secretary.set_conversation("Доброго дня, югаче. Ви принесли необхідні документи")
secretary.set_weakness("довідка")
halytska.set_character(secretary)

big_boss = game.Enemy("Розпорядник", "Людина, що вирішить долю університету.")
big_boss.set_conversation("Покажіть ваш проект")
big_boss.set_weakness("проект")
halytska.set_character(big_boss)

paper = game.Item("довідка")
paper.set_description("Довідка про доходи. Одна зі складових пакету документів для отримання дозволу на землю.")
stryiska.set_item(paper)

police = game.Item("поліцейський")
police.set_description("Може допомогти мені у боротьбі з посіпаками.")
franka.set_item(police)

stick = game.Item("ціпок")
stick.set_description("Бабуся рада добрій справі яку я почав. Але стурбована моєю безпекою. Тому вона "
                      "далє мені свій ціпок для захисту.")
saksahanskoho.set_item(stick)

math = game.Item("математик")
math.set_description("Його гострий розум доповнюється вмінням обговорювати будь-що годинами.")
shevchenka.set_item(math)

project = game.Item("проект")
project.set_description("Він ще знадобиться мені на вулиці Галицькій.")
kniazia_romana.set_item(project)

permission = game.Item("дозвіл")
permission.set_description("Це саме те що мені потрібно, щоб перемогти магната.")
krakivska.set_item(permission)

current_street = kozelnytska
backpack = []

dead = False
command1 = input("> ")
if command1 == "почати":
    while dead is False:
        print("\n")
        current_street.get_details()

        inhabitant = current_street.get_character()
        if inhabitant is not None:
            inhabitant.describe()

        item = current_street.get_item()
        if item is not None:
            item.describe()

        command = input("> ")

        if command in ["північ", "південь", "схід", "захід"]:
            # Move in the given direction
            current_street = current_street.move(command)
        elif command == "говорити":
            # Talk to the inhabitant - check whether there is one!
            if inhabitant is not None:
                inhabitant.touch()
        elif command == "боротись":
            if inhabitant is not None:
                # Fight with the inhabitant, if there is one
                print("За допомогою чого/кого ви будете боротись?")
                fight_with = input()

                # Do I have this item?
                if fight_with in backpack:

                    if inhabitant.fight(fight_with):
                        # What happens if you win?
                        print("Ура! Ви виграли бій!!!")
                        current_street.character = None
                        if game.Item.get_name(permission) and inhabitant.get_defeated() >= 3:
                            print("Вітаємо! Ви перемогли магната! Гра успішно завершина.")
                            dead = True
                    else:
                        # What happens if you lose?
                        print("Ви програли бій.")
                        print("Це кінець гри.")
                        dead = True
                else:
                    print("У вас немає " + fight_with)
            else:
                print("Тут немає з кум боротись.")
        elif command == "взяти":
            if item is not None:
                print("Тепер " + item.get_name() + " з вами")
                backpack.append(item.get_name())
                current_street.set_item(None)
            else:
                print("тут немає,що взяти.")
        else:
            print("На жаль, нема команди " + command)
else:
    print("На жаль, нема команди " + command1)
