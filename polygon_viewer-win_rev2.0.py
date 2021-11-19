from __future__ import print_function

from tkinter import *
from tkinter import filedialog
import tkinter.ttk as ttk
import os
import tkinter.messagebox as msgbox
from PIL import Image, ImageTk, ImageDraw, ImageFont
import json
import keyboard
from pathlib import Path

class frameInit:
    def __init__(self):
        root = Tk() 
        root.title("폴리곤 이미지 Viewer")
        root.geometry('1210x750+150+40') 
        root.resizable(True, True) 

        self.current_path = os.getcwd()

        # top frame
        frame_top = Frame(root, relief = 'solid', bd = 1)
        frame_top.pack(side = 'top', fill = 'both', expand = True)

        # top_left path dir Open frame
        folder_path_frame = LabelFrame(root, text = '작업 폴더 선택')
        folder_path_frame.pack(side = 'top', fill = 'both', pady = 5)

        # select image folder button frame
        image_folder = Frame(folder_path_frame)
        image_folder.pack(side = 'left', fill = 'both')

        image_folder1 = Label(image_folder, text = '이미지 폴더 선택')
        image_folder1.pack(side = 'left', fill = 'both', padx = 5, pady = 5)

        self.image_folder2 = Entry(image_folder, width = 133)
        self.image_folder2.pack(side = 'left', fill = 'both', padx = 5, pady = 5)

        image_folder3 = Button(image_folder, text = '열기', width = 8, command = self.image_dir)
        image_folder3.pack(side = 'left', fill = 'both', padx = 5, pady = 5)

        image_folder4 = Button(image_folder, text = '시작', width = 8, command = self.pre_data_load)
        image_folder4.pack(side = 'left', fill = 'both', padx = 5, pady = 5)

        # # select image folder button frame
        # json_folder = Frame(folder_path_frame)
        # json_folder.pack(side = 'right', fill = 'both')

        # json_folder3 = Button(json_folder, text = '열기', width = 8, command = self.json_dir)
        # json_folder3.pack(side = 'right', fill = 'both', padx = 5, pady = 5)

        # self.json_folder2 = Entry(json_folder, width = 57)
        # self.json_folder2.pack(side = 'right', fill = 'both', padx = 5, pady = 5)

        # json_folder1 = Label(json_folder, text = 'JSON 폴더 선택')
        # json_folder1.pack(side = 'right', fill = 'both', padx = 5, pady = 5)

        # top image info frame
        image_info_frame = LabelFrame(root, text = '이미지 데이터')
        image_info_frame.pack(side = 'top', fill = 'both', pady = 5)

        # image file name frame
        image_info_sub1 = Frame(image_info_frame)
        image_info_sub1.pack(side = 'top', fill = 'both', padx = 5)

        self.folder_name = Label(image_info_sub1, text = '폴더명 :')
        self.folder_name.pack(side = 'left', fill = 'both')

        self.folder_name1 = Label(image_info_sub1, text = '', anchor = 'w', width = 50)
        self.folder_name1.pack(side = 'left', fill = 'both')

        self.image_name = Label(image_info_sub1, text = '파일명 :')
        self.image_name.pack(side = 'left', fill = 'both')

        self.image_name1 = Label(image_info_sub1, text = '', anchor = 'w')
        self.image_name1.pack(side = 'left', fill = 'both')

        # json file info frame
        image_info_sub2 = Frame(image_info_frame)
        image_info_sub2.pack(side = 'top', fill = 'both', padx = 5)

        self.anno_width = Label(image_info_sub2, text = 'width :')
        self.anno_width.pack(side = 'left', fill = 'both')

        self.anno_width1 = Label(image_info_sub2, text = '', anchor = 'w', width = 10)
        self.anno_width1.pack(side = 'left', fill = 'both')

        self.anno_height = Label(image_info_sub2, text = 'height :', anchor = 'w')
        self.anno_height.pack(side = 'left', fill = 'both')

        self.anno_height1 = Label(image_info_sub2, text = '', anchor = 'w', width = 10)
        self.anno_height1.pack(side = 'left', fill = 'both')

        image_info_sub3 = Frame(image_info_sub2)
        image_info_sub3.pack(side = 'left', fill = 'both')

        self.anno_label = Label(image_info_sub3, text = '', anchor = 'w', justify = 'left')
        self.anno_label.pack(side = 'left', fill = 'both', )

        # top_left path dir Open 프레임
        image_view_frame = LabelFrame(root, text = '이미지 뷰어')
        image_view_frame.pack(side = 'top', fill = 'both', pady = 5)

        # image preview frame
        frame_bottom = Frame(image_view_frame, relief = 'solid', bd = 1)
        frame_bottom.pack(side = 'bottom', fill = 'both', expand = True)

        self.bottom_left = Button(frame_bottom, text = '이전', width = 15, command = self.go_pre, state = 'disabled')
        self.bottom_left.pack(side = 'left', fill = 'both', expand = True)

        photo = PhotoImage()
        self.photo_frame = Label(frame_bottom, width = '900', height = '660', bg = 'white', image = photo)
        self.photo_frame.pack(side = 'left', fill = 'both', expand = True)

        self.bottom_right = Button(frame_bottom, text = '다음', width = 15, command = self.go_next, state = 'disabled')
        self.bottom_right.pack(side = 'right', fill = 'both', expand = True)

        keyboard.add_hotkey('left', self.go_pre)
        keyboard.add_hotkey('right', self.go_next)

        root.mainloop()

    def image_dir(self):
        self.image_direct = filedialog.askdirectory(title = '이미지 폴더 열기.', initialdir = self.current_path)
        self.image_folder2.configure(state = 'normal')
        self.image_folder2.delete(0, END)
        self.image_folder2.insert(0, self.image_direct)
        self.image_folder2.configure(state = 'readonly')
        self.folder_name1.configure(text = '')
        self.image_name1.configure(text = '')
        self.anno_width1.configure(text = '')
        self.anno_height1.configure(text = '')
        self.anno_label.configure(text = 'label : {0:<60} type : {1:<25} occluded : {2:<25} z_order : {3:<25} attributes : {4}'.\
                        format('', '', '', '', ''))
        photo = PhotoImage()
        self.photo_frame.configure(image = photo)
        self.photo_frame.image_names = photo

    # def json_dir(self):
    #     self.json_direct = filedialog.askdirectory(title = 'JSON 폴더 열기.', initialdir = self.current_path)
    #     self.json_folder2.configure(state = 'normal')
    #     self.json_folder2.delete(0, END)
    #     self.json_folder2.insert(0, self.json_direct)
    #     self.json_folder2.configure(state = 'readonly')

    def pre_data_load(self):
        folder_order, image_order = 0, 0
        self.data_load(image_order, folder_order)

    def data_load(self, image_order, folder_order):
        self.folder_order = folder_order
        self.image_order = image_order
        if self.image_direct:
            self.img_folders1 = os.listdir(self.image_direct)
            if len(self.img_folders1) != 0:
                if os.path.isdir('{}/{}'.format(self.image_direct, self.img_folders1[self.folder_order])):
                    parent_direct = Path(self.image_direct).parent.absolute()
                    json_files = os.listdir('{}/json'.format(parent_direct))
                    self.img_files = os.listdir('{}/{}'.format(self.image_direct, self.img_folders1[self.folder_order]))
                    for xx in self.img_files:
                        check_path = '{}/{}/{}'.format(self.image_direct, self.img_folders1[self.folder_order], xx)
                        if xx.strip().split('.')[-1] != 'jpg':
                            os.remove(check_path)
                    self.img_files = os.listdir('{}/{}'.format(self.image_direct, self.img_folders1[self.folder_order]))
                    if len(self.img_files) != 0:
                        for i in range(len(json_files)):
                            json_file = json_files[i].strip().split('_')
                            if len(json_file) == 5:
                                target_json = '_'.join([json_file[1], json_file[2], json_file[3], json_file[4]])
                            else:
                                target_json = '_'.join([json_file[0], json_file[1], json_file[2], json_file[3]])
                            if target_json == '{}.json'.format(self.img_folders1[self.folder_order]):
                                self.json_data = json.load(open('{}/json/{}'.format(parent_direct, json_files[i])))
                                break
                            else:
                                self.json_data = {}
                        if self.json_data:
                            self.get_json_data(self.img_folders1[self.folder_order], self.img_files)
                            if self.data_exist == 1:
                                self.load_image(self.img_folders1[self.folder_order], self.img_files[self.image_order])
                                self.bottom_right.configure(state = 'normal')
                        else:
                            msgbox.showwarning('경고', '일치하는 JSON 파일이 없습니다.')
                    else:
                        msgbox.showwarning('경고', '파일이 존재하지 않습니다.')
                        self.bottom_right.configure(state = 'disabled')
                else:
                    parent_direct = Path(self.image_direct).parent.absolute()
                    parent_direct_name = self.image_direct.strip().split('/')[-1]
                    grand_parent_direct = Path(parent_direct).parent.absolute()
                    json_files = os.listdir('{}/json'.format(grand_parent_direct))
                    for xx in self.img_folders1:
                        check_path = '{}/{}'.format(self.image_direct, xx)
                        if xx.strip().split('.')[-1] != 'jpg':
                            os.remove(check_path)
                    self.img_folders1 = os.listdir(self.image_direct)
                    self.img_files = self.img_folders1
                    for i in range(len(json_files)):
                        json_file = json_files[i].strip().split('_')
                        if len(json_file) == 5:
                            target_json = '_'.join([json_file[1], json_file[2], json_file[3], json_file[4]])
                        else:
                            target_json = '_'.join([json_file[0], json_file[1], json_file[2], json_file[3]])
                        if target_json == '{}.json'.format(parent_direct_name):
                            self.json_data = json.load(open('{}/json/{}'.format(grand_parent_direct, json_files[i])))
                            break
                        else:
                            self.json_data = {}
                    if self.json_data:
                        self.get_json_data(parent_direct_name, self.img_files)
                        if self.data_exist == 1:
                            self.load_image1(self.img_files[self.image_order])
                            self.bottom_right.configure(state = 'normal')
                    else:
                         msgbox.showwarning('경고', '일치하는 JSON 파일이 없습니다.')
            else:
                msgbox.showwarning('경고', '폴더 또는 파일이 존재하지 않습니다.')
                self.bottom_right.configure(state = 'disabled')

    def get_json_data(self, img_folder, img_files):
        self.data_exist = 0
        for i in range(len(self.json_data['images'])):
            if self.json_data['images'][i]['name'] == img_files[self.image_order]:
                self.data_exist = 1
                img_name = self.json_data['images'][i]['name']
                img_width = self.json_data['images'][i]['width']
                img_height = self.json_data['images'][i]['height']
                self.img_label = []
                self.img_posi = []
                img_anno_list = []
                self.object_qy = len(self.json_data['images'][i]['objects'])
                for j in range(self.object_qy):
                    self.img_label1 = self.json_data['images'][i]['objects'][j]['label']
                    anno_type1 = self.json_data['images'][i]['objects'][j]['type']
                    self.anno_posi1 = self.json_data['images'][i]['objects'][j]['position'][0]
                    anno_occlu1 = self.json_data['images'][i]['objects'][j]['occluded']
                    anno_z_order1 = self.json_data['images'][i]['objects'][j]['z_order']
                    anno_attri1 = self.json_data['images'][i]['objects'][j]['atrributes']
                    self.img_label.append(self.img_label1)
                    self.img_posi.append(self.anno_posi1)
                    img_anno_sub = [self.img_label1, anno_type1, anno_occlu1, anno_z_order1, anno_attri1]
                    img_anno_list.append(img_anno_sub)
                break
        if self.data_exist == 1:
            self.folder_name1.configure(text = img_folder)
            self.image_name1.configure(text = img_name)
            self.anno_width1.configure(text = img_width)
            self.anno_height1.configure(text = img_height)
            anno_text = ''
            for y in range(len(img_anno_list)):
                if y < len(img_anno_list) - 1:
                    anno_text += 'label : {0:<60} type : {1:<25} occluded : {2:<25} z_order : {3:<25} attributes : {4}\n'.\
                        format(img_anno_list[y][0], img_anno_list[y][1], img_anno_list[y][2], img_anno_list[y][3], img_anno_list[y][4])
                else:
                    anno_text += 'label : {0:<60} type : {1:<25} occluded : {2:<25} z_order : {3:<25} attributes : {4}'.\
                        format(img_anno_list[y][0], img_anno_list[y][1], img_anno_list[y][2], img_anno_list[y][3], img_anno_list[y][4])
                self.anno_label.configure(text = anno_text)
        else:
            msgbox.showwarning('경고', '{}에 매칭되는 json images 항목이 없습니다.'.format(img_files[self.image_order]))

    def load_image(self, img_folder, img_file):
        img_width = 900
        img_height = 660

        image = Image.open('{}/{}/{}'.format(self.image_direct, img_folder, img_file))
        width, height = image.size[0], image.size[1]

        pre_width, pre_height = img_width, int(height * img_width / width)
        resized_img = image.resize((pre_width, pre_height))

        img = ImageDraw.Draw(resized_img)

        var_font = ImageFont.truetype('font/MALGUN.TTF', 20)
        
        for i in range(self.object_qy):
            resized_poly = []
            for j in range(len(self.img_posi[i])):
                x = self.img_posi[i][j] * img_width / width
                resized_poly.append(x)

            resized_poly_x = [resized_poly[i] for i in range(0, len(resized_poly), 2)]
            resized_poly_y = [resized_poly[i + 1] for i in range(0, len(resized_poly), 2)]
            resized_poly = tuple(resized_poly)
            resized_poly_x_min, resized_poly_x_max = min(resized_poly_x), max(resized_poly_x)
            resized_poly_y_min, resized_poly_y_max = min(resized_poly_y), max(resized_poly_y)
            resized_poly_center = ((resized_poly_x_min + resized_poly_x_max) / 2 - 100, (resized_poly_y_min + resized_poly_y_max) / 2 - 20)

            if self.img_label[i] == 'common_road':
                img.polygon(resized_poly, fill = None, outline = 'yellow')
                img.text((resized_poly_center),  self.img_label[i], font = var_font, fill = 'yellow')
            else:
                img.polygon(resized_poly, fill = None, outline = 'pink')
                img.text((resized_poly_center),  self.img_label[i], font = var_font, fill = 'pink')
 
        photo = ImageTk.PhotoImage(resized_img)
        self.photo_frame.configure(image = photo)
        self.photo_frame.image_names = photo

    def load_image1(self, img_file):
        img_width = 900
        img_height = 660

        image = Image.open('{}/{}'.format(self.image_direct, img_file))
        width, height = image.size[0], image.size[1]

        pre_width, pre_height = img_width, int(height * img_width / width)
        resized_img = image.resize((pre_width, pre_height))

        img = ImageDraw.Draw(resized_img)

        var_font = ImageFont.truetype('font/MALGUN.TTF', 20)
        
        for i in range(self.object_qy):
            resized_poly = []
            for j in range(len(self.img_posi[i])):
                x = self.img_posi[i][j] * img_width / width
                resized_poly.append(x)

            resized_poly_x = [resized_poly[i] for i in range(0, len(resized_poly), 2)]
            resized_poly_y = [resized_poly[i + 1] for i in range(0, len(resized_poly), 2)]
            resized_poly = tuple(resized_poly)
            resized_poly_x_min, resized_poly_x_max = min(resized_poly_x), max(resized_poly_x)
            resized_poly_y_min, resized_poly_y_max = min(resized_poly_y), max(resized_poly_y)
            resized_poly_center = ((resized_poly_x_min + resized_poly_x_max) / 2 - 100, (resized_poly_y_min + resized_poly_y_max) / 2 - 20)

            if self.img_label[i] == 'common_road':
                img.polygon(resized_poly, fill = None, outline = 'yellow')
                img.text((resized_poly_center),  self.img_label[i], font = var_font, fill = 'yellow')
            else:
                img.polygon(resized_poly, fill = None, outline = 'pink')
                img.text((resized_poly_center),  self.img_label[i], font = var_font, fill = 'pink')
 
        photo = ImageTk.PhotoImage(resized_img)
        self.photo_frame.configure(image = photo)
        self.photo_frame.image_names = photo

    def load_json_data(self):
        json_path = self.json_direct
        image_folder_list = os.listdir(json_path)

    def go_pre(self):
        self.image_order -= 1
        if self.image_order < 0:
            self.folder_order -= 1
            if self.folder_order < 0:
                self.bottom_left.configure(state = 'disabled')
                self.image_order += 1
                self.folder_order += 1
                msgbox.showwarning('경고', '이전 파일이 존재하지 않습니다.')
            else:
                self.img_files = os.listdir('{}/{}'.format(self.image_direct, self.img_folders1[self.folder_order]))
                self.image_order = len(self.img_files) - 1
                self.data_load(self.image_order, self.folder_order)
        else:
            self.data_load(self.image_order, self.folder_order)

    def go_next(self):
        self.image_order += 1
        if self.image_order >= len(self.img_files):
            self.folder_order += 1
            if self.folder_order >= len(self.img_folders1):
                self.bottom_right.configure(state = 'disabled')
                self.image_order -= 1
                self.folder_order -= 1
                msgbox.showwarning('경고', '다음 파일이 존재하지 않습니다.')
            else:
                self.image_order = 0
                self.data_load(self.image_order, self.folder_order)
        else:
            self.bottom_left.configure(state = 'normal')
            self.data_load(self.image_order, self.folder_order)

frameInit()