import tkinter

window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(width=200,height=200)
window.config(padx=20,pady=20)

weight_label = tkinter.Label()
weight_label.config(text="Enter Your Weight (kg)")
weight_label.pack()

weight_entry = tkinter.Entry()
weight_entry.pack()

height_label = tkinter.Label()
height_label.config(text="Enter Your Height (cm)")
height_label.pack()

height_entry = tkinter.Entry()
height_entry.pack()

def bmi_calculate_button():

    sonuc_label = tkinter.Label()

    weight_ = weight_entry.get()
    height_ = height_entry.get()

    if not weight_ or not height_:
        sonuc_label.config(text="Enter both weight and height!")
        sonuc_label.pack()

    elif weight_ or height_ == float:

        try:
            weight = float(weight_)
            height_0 = float(height_entry.get())
            height_1 = height_0 / 100
            height = height_1**2
            bmi = weight / height
            str_bmi = str(bmi)

            sonuc_label = tkinter.Label()




            if bmi <= 18.4:
                sonuc_label.config(text="Your BMI is {} . Your are underweight".format(str_bmi[:4]))
                sonuc_label.pack()

            elif bmi >18.4 and bmi <=24.9:
                sonuc_label.config(text="Your BMI is {}. Your are normal weight".format(str_bmi[:4]))
                sonuc_label.pack()

            elif bmi > 24.9 and bmi<=39.9:
                sonuc_label.config(text="Your BMI is {}. Your are overweight".format(str_bmi[:4]))
                sonuc_label.pack()

            elif bmi > 39.9:
                sonuc_label.config(text="Your BMI is {}. Your are obese GO EAT SOME HEALTHY SHIT".format(str_bmi[:4]))
                sonuc_label.pack()
        except ValueError:
            sonuc_label.config(text="Enter a valid number!")
            sonuc_label.pack()





calculate_button = tkinter.Button(text="Calculate",command=bmi_calculate_button)
calculate_button.config()
calculate_button.pack()




window.mainloop()