def draw(self, surface):
    action = False
    # mouse position
    pos = pygame.mouse.get_pos()
    self.sound.play(-1)
    # mouse on button detect
    if self.rect.collidepoint(pos):
        # 0 = left click, 1 = middle click, 2 = right click
        if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
            self.clicked = True
            action = True
    if pygame.mouse.get_pressed()[0] == 0:
        self.clicked = False

    # draw button on screen
    surface.blit(self.image, (self.rect.x, self.rect.y))
    return action

def main_window():
    root = Tk()
    root.title("Registration")
    width = 640
    height = 480
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)
    root.bg_image = Image.open("E:/images/Cover_page.png")
    root.bg_image_resized = root.bg_image.resize((640, 480), Image.ADAPTIVE)
    root.resized = ImageTk.PhotoImage(root.bg_image_resized)
    root.bgImg = Label(root, image=root.resized)
    root.bgImg.place(x=0, y=0, relheight=1, relwidth=1)
    # play_icon = PhotoImage(file="images/play-square-button.png")
    # btn_play = Button(root,image=play_icon, relief=GROOVE, borderwidth=0,
    #                     activebackground="black", activeforeground="black")
    # btn_play.place(x=300, y=236, height=64, width=64)
 def new_window():
        win = Toplevel()
        win.title("User Names")
        width = 540
        height = 380
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        win.geometry("%dx%d+%d+%d" % (width, height, x, y))
        win.resizable(0, 0)
        bg_image = Image.open("E:/images/FIELD DESIGNS.png")
        bg_image_resized = bg_image.resize((540, 380), Image.ADAPTIVE)
        resized = ImageTk.PhotoImage(bg_image_resized)
        bgImg = Label(win, image=resized)
        bgImg.place(x=0, y=0, relheight=1, relwidth=1)
        win.mainloop()
    def submit():
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute(
            "INSERT INTO User_name VALUES (:username)",
            {
                'username': username.get()
            })
        conn.commit()
        conn.close()
        messagebox.showinfo("Data Inserted", "Username submitted", parent=root)
        root.withdraw()
        return new_window()
    def LoginForm():
        global username
        LoginFrame = Label(root, bg="#471323")
        LoginFrame.place(x=230, y=250, height=75, width=195)
        lbl_username = Label(LoginFrame, text="Username:", font=('cambria', 25), bd=0, bg="#471323", fg="white")
        lbl_username.grid(row=30, column=5)
        username = Entry(LoginFrame, font=('arial', 20), textvariable="USERNAME", width=15, fg="white",
                         bg="#611A2F")
        username.grid(row=35, column=5)
        Submit_button = Button(root, text="Submit", font=('Cambria', 25), activebackground="#471323", fg="#471323",
                               borderwidth=0, command=submit)
        Submit_button.place(x=230, y=350, width=195)
    # def SubmitBtn():
    #
    #     Submit_button = Button(root, text="Submit", font=('Cambria', 25), activebackground="#471323", fg="#471323",
    #                                 borderwidth=0, command=submit)
    #     Submit_button.place(x=230, y=350, width=195)
    LoginForm()
    root.mainloop()

main_window()
