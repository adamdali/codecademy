using System;

namespace ConsoleGame
{
  class Game : SuperGame
  {
    // Creating the method...
    // 'out' passes arguements to the method as a reference type
    public new static void UpdatePosition(string key, out int xAxis, out int yAxis)
    // 'void' = nothing is to be returned
    {
      switch (key)
      // switch statement used for the 4 possible movements that could be triggered by the arrow keys
      {
      case "DownArrow":
        xAxis = 0;
        yAxis = 1;
        break;
      case "UpArrow":
        xAxis = 0;
        yAxis = -1;
        break;
      case "LeftArrow":
        xAxis = -1;
        yAxis = 0;
        break;
      case "RightArrow":
        xAxis = 1;
        yAxis = 0;
        break;
      default:
        xAxis = 0;
        yAxis = 0;
        break;
        // took a while as the axis' were reversed e.g. "down arrow" should be (x = 0, y = -1)
      }
    }

    public new static char UpdateCursor(string key)
    // 'char' = a single character
    {        
      switch (key)
      // method used to return a symobl each time a certain key is pressed
      {
        case "LeftArrow":
          return '<';
        case "RightArrow":
          return '>';
        case "UpArrow":
          return '^';
        case "DownArrow":
          return 'v';
        default:
          return '?';
      }
    }

    public new static int KeepInBounds(int coordinate, int max)
    //'int coordinate' = current coordinate of icon
    //'int max' = the maximum value
    {
      if (coordinate >= max)
      {
        return max - 1;
      }
      else 
      {
        return coordinate;
      }
    }
    // if the coordinate of the icon is more than or equal to the maximum value of the area of the console, return the icon within 1 movement of the maximum restriction. If not the case, return its true value.
    
    
    public new static bool DidScore(int xchar, int ychar, int xfruit, int yfruit)
    {
      if (xchar == xfruit && xchar == yfruit)
      {
        return true;
      }
      else
      {
        return false;
      }
      //(if the x coordinate of the fruit and the x coordinate of the character are equal) and (the y coordinate of the fruit and the y coordinate of the character are also equal) then they are in the same location which returns a true value indicating the fruit has been caught.
    }
  }
}