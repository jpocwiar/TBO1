"""
Test jednostkowy weryfikujący walidator danych wejściowych.

Ten test weryfikuje funkcję sanitizacji (bleach.clean) używaną w aplikacji Flask
do zapobiegania atakom XSS. Test sprawdza zarówno poprawne, jak i niepoprawne
warianty danych wejściowych.

Walidator jest używany w:
- project/books/views.py (funkcje create_book, edit_book)
- project/customers/views.py (funkcje create_customer, edit_customer)
"""
import unittest
from bleach import clean

class TestXSSPrevention(unittest.TestCase):
    
    def test_xss_prevention(self):
        """Test: kod XSS powinien być usunięty przez sanitizację"""
        malicious_input = "<script>alert('XSS')</script>"
        sanitized = clean(malicious_input, tags=[], strip=True)
        
        self.assertNotIn('<script>', sanitized)
        self.assertNotIn('</script>', sanitized)
        self.assertNotIn('<', sanitized) 
    
    def test_valid_input(self):
        """Test: poprawne dane powinny być zaakceptowane"""
        valid_input = "Jan Kowalski"
        sanitized = clean(valid_input, tags=[], strip=True)
        
        # Poprawne dane powinny pozostać niezmienione
        self.assertEqual(valid_input, sanitized)
    
    def test_html_tags_removed(self):
        """Test: tagi HTML powinny być usunięte"""
        html_input = "<b>Bold text</b>"
        sanitized = clean(html_input, tags=[], strip=True)
        
        self.assertNotIn('<b>', sanitized)
        self.assertNotIn('</b>', sanitized)
        self.assertEqual("Bold text", sanitized)

if __name__ == '__main__':
    unittest.main()