import PySimpleGUI as sg


sg.LOOK_AND_FEEL_TABLE['MyNewTheme'] = {'BACKGROUND': '#2f3036',
										'TEXT': '#ffffff',
										'INPUT': '#1f1f1f',
										'TEXT_INPUT': '#ffffff',
										'SCROLL': '#ffffff',
										'BUTTON': ('white', '#1f1f1f'),
										'PROGRESS': ('#01826B', '#D0D0D0'),
										'BORDER': 0, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
										}


sg.theme('MyNewTheme')


import pyautogui
import time
import cv2
import _thread

def work_function(num_cropping, num_smooth, num_strenght, p_s_t, num_of_clips):

	global do_we_work
	do_we_work = True
	num_of_clips = int(num_of_clips)

	btnNextButton = None
	btnCroppingButton = None
	btnSmoothButton = None
	btnStrengthButton = None
	btnPerspectiveButton = None
	btnStabilizeButton = None

	if do_we_work == False:
		print("Emergency shutdown.")
		return 0

	for i in range(num_of_clips):

		if do_we_work == False:
			print("Emergency shutdown.")
			return 0

		while btnCroppingButton == None:
			if do_we_work == False:
				print("Emergency shutdown.")
				return 0

			print("Looking for a cropping field")
			if btnCroppingButton == None:
				btnCroppingButton = pyautogui.locateOnScreen("img/cropping1.png", grayscale=True, confidence=.8) 
				if btnCroppingButton == None:
					btnCroppingButton = pyautogui.locateOnScreen("img/cropping2.png", grayscale=True, confidence=.8) 
					if btnCroppingButton == None:
						btnCroppingButton = pyautogui.locateOnScreen("img/cropping3.png", grayscale=True, confidence=.8) 

		while btnSmoothButton == None:
			if do_we_work == False:
				print("Emergency shutdown.")
				return 0

			print("Looking for a smooth field")
			if btnSmoothButton == None:
				btnSmoothButton = pyautogui.locateOnScreen("img/smooth1.png", grayscale=True, confidence=.8)
				if btnSmoothButton == None:
					btnSmoothButton = pyautogui.locateOnScreen("img/smooth2.png", grayscale=True, confidence=.8)
					if btnSmoothButton == None:
						btnSmoothButton = pyautogui.locateOnScreen("img/smooth3.png", grayscale=True, confidence=.8)

		while btnStrengthButton == None:
			if do_we_work == False:
				print("Emergency shutdown.")
				return 0

			print("Looking for a strength field")
			if btnStrengthButton == None:
				btnStrengthButton = pyautogui.locateOnScreen("img/strength1.png", grayscale=True, confidence=.8)
				if btnStrengthButton == None:
					btnStrengthButton = pyautogui.locateOnScreen("img/strength2.png", grayscale=True, confidence=.8)
					if btnStrengthButton == None:
						btnStrengthButton = pyautogui.locateOnScreen("img/strength3.png", grayscale=True, confidence=.8)

		while btnPerspectiveButton == None:
			if do_we_work == False:
				print("Emergency shutdown.")
				return 0

			print("Looking for a perspective field")

			# full hd perspective
			if btnPerspectiveButton == None:
				btnPerspectiveButton = pyautogui.locateOnScreen("img/perspective1.png", grayscale=True, confidence=.8)
			# 4k perspective
				if btnPerspectiveButton == None:
					btnPerspectiveButton = pyautogui.locateOnScreen("img/perspective2.png", grayscale=True, confidence=.8)
			# v16 perspective
					if btnPerspectiveButton == None:
						btnPerspectiveButton = pyautogui.locateOnScreen("img/perspective3.png", grayscale=True, confidence=.8)

			# full hd similarity
						if btnPerspectiveButton == None:
							btnPerspectiveButton = pyautogui.locateOnScreen("img/perspective4.png", grayscale=True, confidence=.8)
			# 4k simularity
							if btnPerspectiveButton == None:
								btnPerspectiveButton = pyautogui.locateOnScreen("img/perspective5.png", grayscale=True, confidence=.8)
			# v16 simularity
								if btnPerspectiveButton == None:
									btnPerspectiveButton = pyautogui.locateOnScreen("img/perspective6.png", grayscale=True, confidence=.8)

			# full hd translation
									if btnPerspectiveButton == None:
										btnPerspectiveButton = pyautogui.locateOnScreen("img/perspective7.png", grayscale=True, confidence=.8)
			# 4k translation
										if btnPerspectiveButton == None:
											btnPerspectiveButton = pyautogui.locateOnScreen("img/perspective8.png", grayscale=True, confidence=.8)
			# v16 translation
											if btnPerspectiveButton == None:
												btnPerspectiveButton = pyautogui.locateOnScreen("img/perspective9.png", grayscale=True, confidence=.8)





		while btnStabilizeButton == None:
			if do_we_work == False:
				print("Emergency shutdown.")
				return 0
			print("Looking for a stabilization button.")
			if btnStabilizeButton == None:
				btnStabilizeButton = pyautogui.locateOnScreen("img/stabilize1.png", grayscale=True, confidence=.8)
				if btnStabilizeButton == None:
					btnStabilizeButton = pyautogui.locateOnScreen("img/stabilize2.png", grayscale=True, confidence=.8)
					if btnStabilizeButton == None:
						btnStabilizeButton = pyautogui.locateOnScreen("img/stabilize3.png", grayscale=True, confidence=.8)




		time.sleep(1)
		if btnCroppingButton:
			if do_we_work == False:
				print("Emergency shutdown.")
				return 0    
			tmpCenter = pyautogui.center(btnCroppingButton)
			pyautogui.click(tmpCenter)
			#time.sleep(0.5)
			pyautogui.write(num_cropping) 
			#time.sleep(0.5)


		time.sleep(1)
		if btnSmoothButton:
			if do_we_work == False:
				print("Emergency shutdown.")
				return 0
			tmpCenter = pyautogui.center(btnSmoothButton)
			pyautogui.click(tmpCenter)
			#time.sleep(0.5)
			pyautogui.write(num_smooth) 
			#time.sleep(0.5)



		time.sleep(1)
		if btnStrengthButton:
			if do_we_work == False:
				print("Emergency shutdown.")
				return 0
			tmpCenter = pyautogui.center(btnStrengthButton)
			pyautogui.click(tmpCenter)
			pyautogui.write(num_strenght) 
			#time.sleep(0.5)


		time.sleep(1)
		if btnPerspectiveButton:
			if do_we_work == False:
				print("Emergency shutdown.")
				return 0
			tmpCenter = pyautogui.center(btnPerspectiveButton)
			pyautogui.click(tmpCenter)

			but_Per, but_Sim, but_tran = None, None, None

			while but_Per == None:
				if do_we_work == False:
					print("Emergency shutdown.")
					return 0
				print("Looking for a Per button")

				if but_Per == None:
					but_Per = pyautogui.locateOnScreen("img/per_in_list1.png", grayscale=True, confidence=.8)
					if but_Per == None:
						but_Per = pyautogui.locateOnScreen("img/per_in_list2.png", grayscale=True, confidence=.8)
						if but_Per == None:
							but_Per = pyautogui.locateOnScreen("img/per_in_list3.png", grayscale=True, confidence=.8)

			while but_Sim == None:
				if do_we_work == False:
					print("Emergency shutdown.")
					return 0
				print("Looking for a Sim button")

				if but_Sim == None:
					but_Sim = pyautogui.locateOnScreen("img/sim_in_list1.png", grayscale=True, confidence=.8)
					if but_Sim == None:
						but_Sim = pyautogui.locateOnScreen("img/sim_in_list2.png", grayscale=True, confidence=.8)
						if but_Sim == None:
							but_Sim = pyautogui.locateOnScreen("img/sim_in_list3.png", grayscale=True, confidence=.8)

			while but_tran == None:
				if do_we_work == False:
					print("Emergency shutdown.")
					return 0
				print("Looking for a Tran button")

				if but_tran == None:
					but_tran = pyautogui.locateOnScreen("img/tran_in_list1.png", grayscale=True, confidence=.8)
					if but_tran == None:
						but_tran = pyautogui.locateOnScreen("img/tran_in_list2.png", grayscale=True, confidence=.8)
						if but_tran == None:
							but_tran = pyautogui.locateOnScreen("img/tran_in_list3.png", grayscale=True, confidence=.8)
			
			if p_s_t == 'Perspective':
				tmpCenter = pyautogui.center(but_Per)
				pyautogui.click(tmpCenter)
			elif p_s_t == 'Similarity':
				tmpCenter = pyautogui.center(but_Sim)
				pyautogui.click(tmpCenter)
			elif p_s_t == 'Translation':
				tmpCenter = pyautogui.center(but_tran)
				pyautogui.click(tmpCenter)


		time.sleep(2)
		if btnStabilizeButton:
			tmpCenter = pyautogui.center(btnStabilizeButton)
			pyautogui.click(tmpCenter)

		time.sleep(0.8)

		LocateBool = True
		while LocateBool:
			if do_we_work == False:
				print("Emergency shutdown.")
				return 0
			LocateAnal1 = pyautogui.locateOnScreen("img/analyzing1.png", grayscale=True, confidence=.8)
			LocateAnal2 = pyautogui.locateOnScreen("img/analyzing2.png", grayscale=True, confidence=.8)
			LocateAnal3 = pyautogui.locateOnScreen("img/analyzing3.png", grayscale=True, confidence=.8)
			if LocateAnal1 or LocateAnal2 or LocateAnal3:
				if do_we_work == False:
					print("Emergency shutdown.")
					return 0
				LocateAnal1 = pyautogui.locateOnScreen("img/analyzing1.png", grayscale=True, confidence=.8)
				LocateAnal2 = pyautogui.locateOnScreen("img/analyzing2.png", grayscale=True, confidence=.8)
				LocateAnal3 = pyautogui.locateOnScreen("img/analyzing3.png", grayscale=True, confidence=.8)
				print("Analysis is in progress.")
				time.sleep(0.5)
			else:
				if do_we_work == False:
					print("Emergency shutdown.")
					return 0
				LocateBool = False
				print("Analysis is (seems) complete.")
				time.sleep(0.7)

		time.sleep(0.8)

		LocateBool = True
		while LocateBool:
			if do_we_work == False:
				print("Emergency shutdown.")
				return 0
			LocateAnal1 = pyautogui.locateOnScreen("img/analyzing1.png", grayscale=True, confidence=.8)
			LocateAnal2 = pyautogui.locateOnScreen("img/analyzing2.png", grayscale=True, confidence=.8)
			LocateAnal3 = pyautogui.locateOnScreen("img/analyzing3.png", grayscale=True, confidence=.8)
			if LocateAnal1 or LocateAnal2 or LocateAnal3:
				if do_we_work == False:
					print("Emergency shutdown.")
					return 0
				LocateAnal1 = pyautogui.locateOnScreen("img/analyzing1.png", grayscale=True, confidence=.8)
				LocateAnal2 = pyautogui.locateOnScreen("img/analyzing2.png", grayscale=True, confidence=.8)
				LocateAnal3 = pyautogui.locateOnScreen("img/analyzing3.png", grayscale=True, confidence=.8)
				print("Analysis is in progress.")
				time.sleep(0.5)
			else:
				if do_we_work == False:
					print("Emergency shutdown.")
					return 0
				LocateBool = False
				print("Analysis is (seems) complete.")
				time.sleep(0.7)

		time.sleep(0.8)

		StabilizingBool = True
		while StabilizingBool:
			if do_we_work == False:
				print("Emergency shutdown.")
				return 0
			LocateStab1 = pyautogui.locateOnScreen("img/stabilizing1.png", grayscale=True, confidence=.8)
			LocateStab2 = pyautogui.locateOnScreen("img/stabilizing2.png", grayscale=True, confidence=.8)
			LocateStab3 = pyautogui.locateOnScreen("img/stabilizing3.png", grayscale=True, confidence=.8)
			if LocateStab1 or LocateStab2 or LocateStab3:
				if do_we_work == False:
					print("Emergency shutdown.")
					return 0
				LocateStab1 = pyautogui.locateOnScreen("img/stabilizing1.png", grayscale=True, confidence=.8)
				LocateStab2 = pyautogui.locateOnScreen("img/stabilizing2.png", grayscale=True, confidence=.8)
				LocateStab3 = pyautogui.locateOnScreen("img/stabilizing3.png", grayscale=True, confidence=.8)
				print("Stabilization is in progress.")
				time.sleep(0.5)
			else:
				if do_we_work == False:
					print("Emergency shutdown.")
					return 0
				StabilizingBool = False
				print("Stabilization is (seems) complete.")
				time.sleep(0.7)

		time.sleep(0.8)

		StabilizingBool = True
		while StabilizingBool:
			if do_we_work == False:
				print("Emergency shutdown.")
				return 0
			LocateStab1 = pyautogui.locateOnScreen("img/stabilizing1.png", grayscale=True, confidence=.8)
			LocateStab2 = pyautogui.locateOnScreen("img/stabilizing2.png", grayscale=True, confidence=.8)
			LocateStab3 = pyautogui.locateOnScreen("img/stabilizing3.png", grayscale=True, confidence=.8)
			if LocateStab1 or LocateStab2 or LocateStab3:
				if do_we_work == False:
					print("Emergency shutdown.")
					return 0
				LocateStab1 = pyautogui.locateOnScreen("img/stabilizing1.png", grayscale=True, confidence=.8)
				LocateStab2 = pyautogui.locateOnScreen("img/stabilizing2.png", grayscale=True, confidence=.8)
				LocateStab3 = pyautogui.locateOnScreen("img/stabilizing3.png", grayscale=True, confidence=.8)
				print("Stabilization is in progress.")
				time.sleep(0.5)
			else:
				if do_we_work == False:
					print("Emergency shutdown.")
					return 0
				StabilizingBool = False
				print("Stabilization is (seems) complete.")
				time.sleep(0.7)

		print("Done: " + str(i+1) + "/" + str(num_of_clips))

		if i+1 != num_of_clips:
			pyautogui.press('down')


	print("\n\nAll Done")




layout = [[sg.Text('Cropping'), sg.Input("0.5", size=(4, 1)), sg.Text('Smooth'), sg.Input("0.25", size=(4, 1)), sg.Text('Strenght'),sg.Input("1", size=(4, 1))],
		  [sg.InputCombo(('Perspective', 'Similarity', 'Translation'), "Perspective", size=(12, 1))],
		  [sg.Text('How many clips to stabilize?'), sg.Input("1", size=(3, 1))],
		  [sg.Output(size=(40,9))],
		  [sg.Button("Start"), sg.Button('STOP'), sg.Button('?'), sg.Button('Close'), sg.Text('       v6 by Alzakprod.')]]


window = sg.Window('Stabilizing Automation', layout, keep_on_top=True, icon='img/logo.ico')

global do_we_work 

while True:
	event, values = window.read()
	if event == "?":
		print('\n\nWork with v16 4k, v17 fhd, v17 4k\nyou can change buttons img, but it is hard)\n\nBefore start:\nOpen Davinci\nOpen "Color" tab\nOpen "Stab" tab\nSet the first clip')
	if event == "Start":
		do_we_work = True
		print(values[0], values[1], values[2], values[3], values[4])
		try:
			if int(values[4]) < 1:
				print("Change count of clips!!!")
			else:
				_thread.start_new_thread(work_function, (values[0], values[1], values[2], values[3], values[4]))
		except:
			print("Error in arguments")


	if event == "STOP":
		do_we_work = False
		print("Emergency shutdown requested.")

	if event == sg.WINDOW_CLOSED or event == 'Close':
		do_we_work = False
		break
window.close()