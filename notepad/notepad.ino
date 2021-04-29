#include <Keyboard.h>

void typeKey(uint8_t key)
{
  Keyboard.press(key);
  delay(50);
  Keyboard.release(key);
}

/* Init function */
void setup()
{
  // Begining the Keyboard stream
  Keyboard.begin();

  // Wait 500ms
  delay(500);

  // First Duck
  delay(500);
  Keyboard.press(KEY_LEFT_GUI);
  Keyboard.press('r');
  Keyboard.releaseAll();

  delay(500);
  Keyboard.print("notepad.exe");

  delay(500);
  typeKey(KEY_RETURN);

  delay(500);
  Keyboard.print("Hello World!");

  // Ending stream
  Keyboard.end();
}

/* Unused endless loop */
void loop() {}
