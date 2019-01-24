# Temainnlevering 1

# Oppgave 1
print("Sondre")
print("Knutsen\n")

print("Sondre\nKnutsen\n")

f = "Sondre"
e = "Knutsen\n"
print(f, e, sep="\n")


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
euro = '%.2f' % (x * 25.60 / 250)
dollar = '%.2f' % (x * 29.05 / 250)
print(x, "kroner tilsvarer ", euro, " Euro og ", dollar, " Dollar\n", sep="")


# Oppgave 3b
print("NOK", x, "tilsvarer ", euro, u"\N{euro sign} og ", dollar, u"\N{dollar sign}",  sep="")
