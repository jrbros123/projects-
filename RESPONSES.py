from random import choice, randint

def get_random_bible_verse():
    verses = [
        "John 3:16 - For God so loved the world, that he gave his only Son, that whoever believes in him should not perish but have eternal life.",
        "Philippians 4:13 - I can do all things through him who strengthens me.",
        "Jeremiah 29:11 - For I know the plans I have for you, declares the Lord, plans for welfare and not for evil, to give you a future and a hope.",
        "Romans 8:28 - And we know that in all things God works for the good of those who love him, who have been called according to his purpose.",
        "Proverbs 3:5-6 - Trust in the Lord with all your heart, and do not lean on your own understanding. In all your ways acknowledge him, and he will make straight your paths.",
        "Psalm 23:1 - The Lord is my shepherd; I shall not want.",
        "Isaiah 41:10 - Fear not, for I am with you; be not dismayed, for I am your God; I will strengthen you, I will help you, I will uphold you with my righteous right hand.",
        "Matthew 11:28 - Come to me, all who labor and are heavy laden, and I will give you rest.",
        "2 Corinthians 5:7 - For we walk by faith, not by sight.",
        "1 Peter 5:7 - Cast all your anxieties on him, because he cares for you."
        "Isaiah 40:31 - But they who wait for the Lord shall renew their strength; they shall mount up with wings like eagles; they shall run and not be weary; they shall walk and not faint.",
        "Joshua 1:9 - Have I not commanded you? Be strong and courageous. Do not be frightened, and do not be dismayed, for the Lord your God is with you wherever you go.",
        "Psalm 46:1 - God is our refuge and strength, a very present help in trouble.",
        "1 Corinthians 13:4-5 - Love is patient and kind; love does not envy or boast; it is not arrogant or rude. It does not insist on its own way; it is not irritable or resentful.",
        "2 Timothy 1:7 - For God gave us a spirit not of fear but of power and love and self-control.",
        "Romans 12:2 - Do not be conformed to this world, but be transformed by the renewal of your mind, that by testing you may discern what is the will of God, what is good and acceptable and perfect.",
        "Matthew 6:33 - But seek first the kingdom of God and his righteousness, and all these things will be added to you.",
        "Ephesians 2:8-9 - For by grace you have been saved through faith. And this is not your own doing; it is the gift of God, not a result of works, so that no one may boast.",
        "Psalm 119:105 - Your word is a lamp to my feet and a light to my path.",
        "Proverbs 18:10 - The name of the Lord is a strong tower; the righteous man runs into it and is safe.",
        "John 14:27 - Peace I leave with you; my peace I give to you. Not as the world gives do I give to you. Let not your hearts be troubled, neither let them be afraid.",
        "1 John 4:18 - There is no fear in love, but perfect love casts out fear. For fear has to do with punishment, and whoever fears has not been perfected in love.",
        "James 1:5 - If any of you lacks wisdom, let him ask God, who gives generously to all without reproach, and it will be given him.",
        "Philippians 4:6-7 - Do not be anxious about anything, but in everything by prayer and supplication with thanksgiving let your requests be made known to God. And the peace of God, which surpasses all understanding, will guard your hearts and your minds in Christ Jesus.",
        "Hebrews 11:1 - Now faith is the assurance of things hoped for, the conviction of things not seen."
    ]
    return choice(verses)

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Well, you\'re awfully silent...'
    elif 'hello' in lowered:
        return 'Hello there!'
    elif 'how are you' in lowered:
        return 'Good, thanks!'
    elif 'gimme a bible verse' in lowered:
        return get_random_bible_verse()
    elif 'bye' in lowered:
        return 'See you!'
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1, 6)}'
    elif 'bose is gay' in lowered:
        return 'That is true!'
    else:
        return choice(['I do not understand...',
                       'What are you talking about?',
                       'Do you mind rephrasing that?'])
