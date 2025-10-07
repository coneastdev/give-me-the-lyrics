import unittest
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from app import getLyrics

class TestLyricOutput(unittest.TestCase):
    
    def test_lyrics_equal_stayin(self): # should equal  Bee Gees sating alive
        expected_lyrics = ("[Verse 1] Well, you can tell by the way I use my walk I'm a woman's man, no time to talk The music loud and the women warm I've been kicked around since I was born [Pre-Chorus] And now it's alright, it's okay And you may look the other way But we can try to understand The New York Times' effect on man [Chorus] Whether you're a brother or whether you're a mother You're stayin' alive, stayin' alive Feel the city breakin' and everybody shakin' And we're stayin' alive, stayin' alive Ah, ah, ah, ah Stayin' alive, stayin' alive Ah, ah, ah, ah Stayin' alive Oh, when you walk [Verse 2] Well now, I get low and I get high And if I can't get either, I really try Got the wings of Heaven on my shoes I'm a dancin' man and I just can't lose [Pre-Chorus] You know it's alright, it's okay I'll live to see another day But we can try to understand The New York Times' effect on man [Chorus] Whether you're a brother or whether you're a mother You're stayin' alive, stayin' alive Feel the city breakin' and everybody shakin' And we're stayin' alive, stayin' alive Ah, ah, ah, ah Stayin' alive, stayin' alive Ah, ah, ah, ah Stayin' alive (Hey, yeah) [Bridge] Life goin' nowhere Somebody help me Somebody help me, yeah Life goin' nowhere Somebody help me, yeah I'm stayin' alive [Verse 1] Well, you can tell by the way I use my walk I'm a woman's man, no time to talk The music loud and the women warm I've been kicked around since I was born [Pre-Chorus] And now it's alright, it's okay And you may look the other way But we can try to understand The New York Times' effect on man [Chorus] Whether you're a brother or whether you're a mother You're stayin' alive, stayin' alive Feel the city breakin' and everybody shakin' And we're stayin' alive, stayin' alive Ah, ah, ah, ah Stayin' alive, stayin' alive Ah, ah, ah, ah Stayin' alive (Hey, yeah) [Outro] Life goin' nowhere Somebody help me Somebody help me, yeah Life goin' nowhere Somebody help me, yeah I'm stayin' alive Life goin' nowhere Somebody help me Somebody help me, yeah Life goin' nowhere Somebody help me, yeah I'm stayin' alive Life goin' nowhere Somebody help me Somebody help me, yeah Life goin' nowhere Somebody help me, yeah I'm stayin' alive Life goin' nowhere Somebody help me Somebody help me, yeah Life goin' nowhere Somebody help me, yeah I'm stayin' alive").replace(" ", "")
        actual_lyrics = (getLyrics("Stayin").replace("\n", " ")).replace(" ", "")
        self.assertEqual(actual_lyrics, expected_lyrics)

    def test_lyrics_equal_never(self): # should equal  Rick Astley never gonna give you up
        expected_lyrics = ("[Intro]Desert youOoh-ooh-ooh-oohHurt you[Verse 1]We're no strangers to loveYou know the rules and so do I (Do I)A full commitment's what I'm thinking ofYou wouldn't get this from any other guy[Pre-Chorus]I just wanna tell you how I'm feelingGotta make you understand[Chorus]Never gonna give you upNever gonna let you downNever gonna run around and desert youNever gonna make you cryNever gonna say goodbyeNever gonna tell a lie and hurt you[Verse 3]We've known each other for so longYour heart's been aching, but you're too shy to say it (To say it)Inside, we both know what's been going on (Going on)We know the game, and we're gonna play it [Pre-Chorus]And if you ask me how I'm feelingDon't tell me you're too blind to see[Chorus]Never gonna give you upNever gonna let you downNever gonna run around and desert youNever gonna make you cryNever gonna say goodbyeNever gonna tell a lie and hurt youNever gonna give you upNever gonna let you downNever gonna run around and desert youNever gonna make you cryNever gonna say goodbyeNever gonna tell a lie and hurt you[Bridge]Ooh (Give you up)Ooh-ooh (Give you up)Ooh-oohNever gonna give, never gonna give (Give you up)Ooh-oohNever gonna give, never gonna give (Give you up)[Verse 2]We've known each other for so longYour heart's been aching, but you're too shy to say it (To say it)Inside, we both know what's been going on (Going on)We know the game, and we're gonna play it[Pre-Chorus]I just wanna tell you how I'm feelingGotta make you understand[Chorus]Never gonna give you upNever gonna let you downNever gonna run around and desert youNever gonna make you cryNever gonna say goodbyeNever gonna tell a lie and hurt youNever gonna give you upNever gonna let you downNever gonna run around and desert youNever gonna make you cryNever gonna say goodbyeNever gonna tell a lie and hurt youNever gonna give you upNever gonna let you downNever gonna run around and desert youNever gonna make you cryNever gonna say goodbyeNever gonna tell a lie and hurt you").replace(" ", "")
        actual_lyrics = (getLyrics("never gonna").replace("\n", " ")).replace(" ", "")
        self.assertEqual(actual_lyrics, expected_lyrics)

    def test_lyricadvisor_lyrics_equal_stayin(self): # should equal  Bee Gees sating alive
        expected_lyrics = ("Well, you can tell by the way I use my walk I'm a woman's man, no time to talk. Music loud and women warm, I've been kicked around since I was born. And now it's all right, thats okay, you may look the other way. We can try to understand the New York Times' effect on man. (Chorus) Whether you're a brother or whether you're a mother you're stayin' alive, stayin' alive. Feel the city breakin' and everybody shakin' and you're stayin' alive, stayin' alive. Ah, ah, ah, ah, stayin' alive, stayin' alive, ah, ah, ah, ah, stayin' alive. Oh, when you walk. Well, now I get low and I get high, and if I can't get either, I really try. Got the wings of heaven on my shoes, I'm a dancin' man and I just can't lose. You know, it's all right, it's okay, I'll live to see another day. We can try to understand the New York Times' effect on man. (Repeat chorus) (Bridge) Life goin' nowhere, somebody help me, somebody help me, yeah. Life goin' nowhere, somebody help me, yeah. I'm stayin' alive. (Repeat first verse) (Repeat chorus) (Repeat bridge and fade)").replace(" ", "")
        actual_lyrics = (getLyrics("Stayin", source="lyricadvisor").replace("\n", " ")).replace(" ", "")
        self.assertEqual(actual_lyrics, expected_lyrics)

    def test_lyricadvisor_lyrics_equal_never(self): # should equal  Rick Astley never gonna give you up
        expected_lyrics = ("We're no strangers to love You know the rules and so do I A full commitment's what I'm thinking of You wouldn't get this from any other guy I just wanna tell you how I'm feeling Gotta make you understand CHORUS Never gonna give you up, Never gonna let you down, Never gonna run around and desert you, Never gonna make you cry, Never gonna say goodbye, Never gonna tell a lie and hurt you We've known each other for so long Your heart's been aching but you're too shy to say it Inside we both know what's been going on We know the game and we're gonna play it And if you ask me how I'm feeling Don't tell me you're too blind to see (CHORUS) CHORUSCHORUS (Ooh give you up) (Ooh give you up) (Ooh) never gonna give, never gonna give (give you up) (Ooh) never gonna give, never gonna give (give you up) We've known each other for so long Your heart's been aching but you're too shy to say it Inside we both know what's been going on We know the game and we're gonna play it I just wanna tell you how I'm feeling Gotta make you understand (CHORUS)").replace(" ", "")
        actual_lyrics = (getLyrics("never gonna", source="lyricadvisor").replace("\n", " ")).replace(" ", "")
        self.assertEqual(actual_lyrics, expected_lyrics)

    # Generated with chatgpt-4.1 with co-pilot
    
    def test_song_not_found(self):
        """Test that a nonsense query returns an empty string or appropriate message."""
        actual_lyrics = getLyrics("asdkfjhasdkjfhaskjdhf")  # unlikely to match any song
        self.assertTrue(actual_lyrics.strip() == "" or "not found" in actual_lyrics.lower())

    def test_partial_query(self):
        """Test that a partial query returns some lyrics."""
        actual_lyrics = getLyrics("Bohemian")  # partial for 'Bohemian Rhapsody'
        self.assertTrue(len(actual_lyrics.strip()) > 0)

    def test_special_characters_query(self):
        """Test that queries with special characters do not break the function."""
        actual_lyrics = getLyrics("Happier!@#")  # song with special chars
        self.assertIsInstance(actual_lyrics, str)

    def test_empty_query(self):
        """Test that an empty query returns an empty string or appropriate message."""
        actual_lyrics = getLyrics("")
        self.assertTrue(actual_lyrics.strip() == "" or "not found" in actual_lyrics.lower())
    
    def test_numeric_query(self):
        """Test that numeric queries do not break the function."""
        actual_lyrics = getLyrics("12345")
        self.assertIsInstance(actual_lyrics, str)

    def test_non_ascii_query(self):
        """Test that non-ASCII queries do not break the function."""
        actual_lyrics = getLyrics("Despacitoñ")
        self.assertIsInstance(actual_lyrics, str)

    def test_long_query(self):
        """Test that a very long query string does not break the function."""
        long_query = "a" * 1000
        actual_lyrics = getLyrics(long_query)
        self.assertTrue(actual_lyrics.strip() == "" or "not found" in actual_lyrics.lower())

    def test_multiple_word_query(self):
        """Test that a multi-word query returns lyrics."""
        actual_lyrics = getLyrics("Bohemian Rhapsody")
        self.assertTrue(len(actual_lyrics.strip()) > 0)

    def test_query_with_apostrophe(self):
        """Test that queries with apostrophes work."""
        actual_lyrics = getLyrics("Don't Stop Believin'")
        self.assertIsInstance(actual_lyrics, str)
    
    def test_lyricadvisor_known_song(self):
        """Test lyricadvisor source with a known song."""
        lyrics = getLyrics("We Didn't Start the Fire", source="lyricadvisor")
        self.assertIn("We didn't start the fire", lyrics)

    def test_lyricadvisor_song_not_found(self):
        """Test lyricadvisor source with a nonsense query."""
        lyrics = getLyrics("asdkfjhasdkjfhaskjdhf", source="lyricadvisor")
        self.assertTrue(lyrics.strip() == "" or "not found" in lyrics.lower())

    def test_lyricadvisor_empty_query(self):
        """Test lyricadvisor source with empty query."""
        lyrics = getLyrics("", source="lyricadvisor")
        self.assertTrue(lyrics.strip() == "" or "not found" in lyrics.lower())
    
    # End of AI generated tests

if __name__ == '__main__':
    unittest.main()