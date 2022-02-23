using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PiatraFoarfecaHartie
{
    class Program
    {
        static void Main(string[] args)
        {
            string Jucator,Cpu;
            int randomNr;

            bool jocNou = true;

            while (jocNou)
            {
                int scorJucator= 0;
                int scorCpu = 0;

                while (scorJucator < 3 && scorCpu < 3)
                {
                    Console.Write("Alege dintre Piatra, Hartie si Foarfeca: ");
                    Jucator = Console.ReadLine();
                    Jucator = Jucator.ToUpper();

                    Random rnd = new Random();

                    randomNr = rnd.Next(1, 4);

                    switch (randomNr)
                    {
                        case 1:
                            Cpu = "Piatra";
                            Console.WriteLine("Calculatorul a ales Piatra");
                            if (Jucator == "Piatra")
                            {
                                Console.WriteLine("Remiza!!\n\n");
                            }
                            else if (Jucator == "Hartie")
                            {
                                Console.WriteLine("Jucatorul castiga!!\n\n");
                                scorJucator++;
                            }
                            else if (Jucator == "Foarfeca")
                            {
                                Console.WriteLine("Calculatorul a castigat!!\n\n");
                                scorCpu++;
                            }
                            break;
                        case 2:
                            Cpu = "Hartie";
                            Console.WriteLine("Calculatorul a ales Hartie");
                            if (Jucator == "Hartie")
                            {
                                Console.WriteLine("Remiza!!\n\n");
                            }
                            else if (Jucator == "Piatra")
                            {
                                Console.WriteLine("Calculatorul castiga !!\n\n");
                                scorCpu++;
                            }
                            else if (Jucator == "Foarfeca")
                            {
                                Console.WriteLine("Jucatorul castiga!!\n\n");
                                scorJucator++;
                            }
                            break;
                        case 3:
                            Cpu = "Foarfeca";
                            Console.WriteLine("Calculatorul a ales Foarfeca");
                            if (Jucator == "Foarfeca")
                            {
                                Console.WriteLine("Remiza!!\n\n");
                            }
                            else if (Jucator == "Piatra")
                            {
                                Console.WriteLine("Jucatorul Castiga!!\n\n");
                                scorJucator++;
                            }
                            else if (Jucator == "Hartie")
                            {
                                Console.WriteLine("Calculatorul castiga!!\n\n");
                                scorCpu++;
                            }
                            break;
                        default:
                            Console.WriteLine("Optiune invalida!");
                            break;
                    }

                    Console.WriteLine("\n\nScoruri:\tJucator:\t{0}\tCPU:\t{1}", scorJucator, scorCpu);

                }

                if (scorJucator == 3)
                {
                    Console.WriteLine("Jucatorul a castigat!");
                }
                else if (scorCpu == 3)
                {
                    Console.WriteLine("Calculatorul a castigat");
                }
             
                Console.WriteLine("Vrei sa joci din nou ?(d/n)");
                string loop = Console.ReadLine();
                if (loop == "d")
                {
                    jocNou = true;
                    Console.Clear();
                }
                else if (loop == "n")
                {
                    jocNou = false;
                }
            }
        }
    }
}