# kursach-vsp
Calculation of the joint-free railway track for strength.			
			Цели: создать сайт, в который пользователь вбивает исходные данные по данной курсовой работе и за символическую плату получает расчеты.
			Достигнуто: Код позволяет вывести расчеты и графики к ним практически по всей курсовой, что значительно ускоряет процесс.
			Текущие задачи: Выяснить, какие инструменты лучше подойдут новичку для этих целей. Какая база данных способна работать с питон и веб-сайтом(принимать, хранить и передавать переменные в этот код-бэкенд)? 
			Какой фреймворк\библиотека соеденит интерфейс сайта, базу данных и текущие расчеты(бэкенд в репо)?
			ОПИСАНИЕ: main - хранит исходные и выводит расчеты, initial_data тоже хранит переменные и производит расчеты
gragic_progibov, grafic_Izgib_moments - принимает переменную k, к сожалению, вручную вбиваю (ее бы как-нибудь унаследовать от initial_data, но как?) и выводит графики
helper - просто вспомогательное для написания кода окно
