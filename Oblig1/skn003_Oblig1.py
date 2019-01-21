# Temainnlevering 1

# Oppgave 1
print("Sondre")
print("Knutsen\n")

print("Sondre\nKnutsen\n")

f = "Sondre"
e = "\nKnutsen"
print(f, e, "\n")


# Oppgave 2
ascii_text = """\
 *****                                      
*     *  ****  *    * *****  *****  ****** 
*       *    * **   * *    * *    * *      
 *****  *    * * *  * *    * *    * ***** 
      * *    * *  * * *    * *****  *     
*     * *    * *   ** *    * *   *  *       
 *****   ****  *    * *****  *    * ******                                                                                         
"""
print(ascii_text)


# Oppgave 3a
x = 250
print(x, "kroner tilsvarer " + '%.2f' % (x * 25.60 / 250) + " Euro og " + '%.2f' % (x * 29.05 / 250) + " Dollar\n")


# Oppgave 3b
print("NOK", x, "tilsvarer " + '%.2f' % (x * 25.60 / 250) + u"\N{euro sign} og " + '%.2f' % (x * 29.05 / 250) + u"\N{dollar sign}")
