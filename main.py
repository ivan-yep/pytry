from newspapers.newspaper import Newspaper
from newspapers.newspaper_with_title import NewspaperWithTitle

def main():
    regular_newspaper = Newspaper(20)
    regular_newspaper.add_text_chunk('01234567890123456789')
    regular_newspaper.add_text_chunk('Hi')
    regular_newspaper.add_text_chunk("Hi, how's your day")
    regular_newspaper.add_text_chunk('AUGHHHH')
    regular_newspaper.add_text_chunk("gonna get sticky")
    regular_newspaper.add_text_chunk('BY THE EYE OFAGAMOTO')
    regular_newspaper.add_text_chunk('the moon')
    regular_newspaper.add_text_chunk('I say the moon')
    regular_newspaper.add_text_chunk('haunts, you!')
    print(regular_newspaper)

    print()

    title_newspaper = NewspaperWithTitle(20, 'Gaming')
    title_newspaper.add_text_chunk("gonna get sticky")
    title_newspaper.add_text_chunk('BY THE EYE OFAGAMOTO')
    title_newspaper.add_text_chunk('the moon')
    title_newspaper.add_text_chunk('haunts you')
    print(title_newspaper)

    print()

    title_newspaper.set_title('who asked')
    print(title_newspaper)

if __name__ == '__main__':
    main()