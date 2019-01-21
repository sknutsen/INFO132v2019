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
def currency_print(x):
    euro = x * 25.62 / 250
    dollar = x * 29.05 / 250
    print(x, "kroner tilsvarer", euro, "Euro og", dollar, "Dollar.\n")


currency_print(250)


# Oppgave 3b
def currency_print2(x):
    euro = x * 25.62 / 250
    dollar = x * 29.05 / 250
    print("NOK", x, "tilsvarer", euro, u"\N{euro sign}", "og", dollar, u"\N{dollar sign}")


currency_print2(250)
