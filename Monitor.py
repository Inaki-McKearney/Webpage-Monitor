from urllib.request import urlopen
import EmailAlert


class Changes:
    def __init__(self, url, archive='archived_page.html'):
        self.url = url
        self.new_html = []
        self.old_html = []
        self.change_list = []
        self.archive = archive

    def update(self):
        with urlopen(self.url) as byt:
            self.new_html = [x.decode('latin-1') for x in byt.readlines()]

        open(self.archive, 'a').close()

        with open(self.archive, 'rb+') as old:
            self.old_html = [x.decode('latin-1') for x in old.readlines()]
            old.seek(0)
            old.truncate()
            old.writelines(x.encode('latin-1') for x in self.new_html)

    def diff(self):
        self.change_list = []
        for a, b in zip(self.old_html, self.new_html):
            if a != b:
                if not b.strip():
                    self.change_list.append(f'\nLine removed:\n{a}\n')
                elif not a.strip():
                    self.change_list.append(f'\nLine added:\n{b}\n')
                else:
                    self.change_list.append(f'\n{a}Changed to:\n{b}\n')
        return self.change_list

    def email(self):
        message = f'{len(self.change_list)} changes in {self.url}:\n'
        message += ''.join(self.change_list)
        EmailAlert.send(message)


if __name__ == '__main__':
    link = 'https://en.wikipedia.org/wiki/Main_Page'
    wiki_updater = Changes(link)
    wiki_updater.update()
    if wiki_updater.diff():
        wiki_updater.email()
