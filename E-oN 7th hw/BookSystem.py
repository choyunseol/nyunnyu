import pandas as pd

class System():
    def __init__(self):
        self.txt = pd.read_csv('input.txt', header=None, sep=" ", engine='python', encoding='CP949')
        self.txt.columns = ['title', 'author', 'year', 'publisher', 'genre']

    def add(self):
        book_info = input("책제목, 저자, 출판 연도, 출판사, 장르 를 순서대로 입력하세요 (띄어쓰기로 구분):").split(" ")
        add_book_info = pd.DataFrame(data=[book_info], columns=self.txt.columns)
        self.txt = self.txt.append(add_book_info)
        self.txt = self.txt.reset_index(drop=True)
        print(self.txt)
        print('저장을 원하시면 메뉴에서 "도서 목록 저장"을 선택하세요')

    def search(self):
        Wanna_Get = input('어떤 특징의 책을 찾습니까?\n숫자를 입력해주세요.\n1.도서명\n2.저자\n3.출판연도\n4.출판사명\n5.장르\n')
        while not (Wanna_Get == '1' or Wanna_Get == '2' or Wanna_Get == '3' or Wanna_Get == '4' or Wanna_Get == '5'):
            Wanna_Get = input('어떤 특징의 책을 찾습니까?\n숫자를 입력해주세요.\n1.도서명\n2.저자\n3.출판연도\n4.출판사명\n5.장르\n')
        if Wanna_Get == '1':
            search_title = input('찾는 책의 이름을 입력해주세요 :')
            print(self.txt.loc[self.txt['title'] == search_title])
        elif Wanna_Get == '2':
            search_author = input('찾는 책의 저자를 입력해주세요 :')
            print(self.txt.loc[self.txt['author'] == search_author])
        elif Wanna_Get == '3':
            search_year = int(input('찾는 책의 출판 연도를 입력해주세요 :'))
            print(self.txt.loc[self.txt['year'] == search_year])
        elif Wanna_Get == '4':
            search_publisher = input('찾는 책의 출판사를 입력해주세요 :')
            print(self.txt.loc[self.txt['publisher'] == search_publisher])
        elif Wanna_Get == '5':
            search_genre = input('찾는 책의 장르를 입력해주세요 :')
            print(self.txt.loc[self.txt['genre'] == search_genre])

    def modify(self):
        Wanna_modify = input('수정할 책의 이름을 띄어쓰기 없이 입력하세요 :')
        What_modify = input('어떤 정보를 수정하시겠습니까?\n숫자를 입력해주세요.\n1.도서명\n2.저자\n3.출판연도\n4.출판사명\n5.장르\n')

        index = self.txt.index[self.txt['title'] == Wanna_modify]
        if What_modify == '1':
            self.txt.at[index, 'title'] = input('책의 이름을 띄어쓰기 없이 입력하세요 :')
            print(self.txt)
        elif What_modify == '2':
            self.txt.at[index, 'author'] = input('저자를 띄어쓰기 없이 입력하세요 :')
            print(self.txt)
        elif What_modify == '3':
            self.txt.at[index, 'year'] = input('출판 연도를 띄어쓰기 없이 입력하세요 :')
            print(self.txt)
        elif What_modify == '4':
            self.txt.at[index, 'publisher'] = input('출판사를 띄어쓰기 없이 입력하세요 :')
            print(self.txt)
        elif What_modify == '5':
            self.txt.at[index, 'genre'] = input('장르를 띄어쓰기 없이 입력하세요 :')
            print(self.txt)
        else:
            self.modify()
        print('저장을 원하시면 메뉴에서 "도서 목록 저장"을 선택하세요')

    def delete(self):
        Wanna_delete = input('삭제할 책의 이름을 띄어쓰기 없이 입력하세요 :')
        self.txt = self.txt.drop(self.txt.index[self.txt['title'] == Wanna_delete])
        self.txt = self.txt.reset_index(drop=True)
        print(self.txt)
        print('저장을 원하시면 메뉴에서 "도서 목록 저장"을 선택하세요')


    def print_all(self):
        print(self.txt)

    def save(self):
        save = input('저장하시겠습니까? 예:1 아니오:2 \n')
        if save == '1':
            self.txt.to_csv('input.txt', sep=' ', header=None, index=False, encoding='CP949')
        elif save == '2':
            exit
        else:
            self.save()

    def auto_save(self):
            self.txt.to_csv('input.txt', sep=' ', header=None, index=False, encoding='CP949')

    def selection(self):
        select = input('1. 도서 추가\n2. 도서검색\n3. 도서 정보 수정\n4. 도서 삭제\n5. 현재 총 도서 목록 출력\n6. 도서 목록 저장\n')

        if select == '1':
            self.add()
        elif select == '2':
            self.search()
        elif select == '3':
            self.modify()
        elif select == '4':
            self.delete()
        elif select == '5':
            self.print_all()
        elif select == '6':
            self.save()
        else:
            self.selection()