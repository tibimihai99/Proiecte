﻿using OpenTK;
using System;
using System.Drawing;

namespace Lab_5
{
    public class Randomizer
    {
        private Random r;

        private const int MIN_VAL = -25;
        private const int MAX_VAL = 25;

        private const int LOW_INT_VAL = -25;
        private const int HIGH_INT_VAL = 25;
        private const int LOW_COORD_VAL = -50;
        private const int HIGH_COORD_VAL = 50;

       
        public Randomizer()
        {
            r = new Random();
        }

        public Color RandomColor()
        {
            int genR = r.Next(0, 255);
            int genG = r.Next(0, 255);
            int genB = r.Next(0, 255);

            Color culoare = Color.FromArgb(genR, genG, genB);

            return culoare;
        }

        public int GetRandomOffsetPositive(int maxval)
        {
            int genInteger = r.Next(0, maxval);

            return genInteger;
        }

        public int GetRandomOffsetRanged(int maxval)
        {
            int genInteger = r.Next(-1 * maxval, maxval);

            return genInteger;
        }

        public Vector3 Generate3DPoint()
        {
            int a = r.Next(MIN_VAL, MAX_VAL);
            int b = r.Next(MIN_VAL, MAX_VAL);
            int c = r.Next(MIN_VAL, MAX_VAL);

            Vector3 vector = new Vector3(a, b, c);

            return vector;
        }

        public Vector3 Generate3DPoint(int spec)
        {
            int a = r.Next(-1 * spec, spec);
            int b = r.Next(-1 * spec, spec);
            int c = r.Next(-1 * spec, spec);

            Vector3 vector = new Vector3(a, b, c);

            return vector;
        }

        public int GeneratePositiveInt(int limit)
        {
            return r.Next(0, limit);
        }

      
        public int RandomInt()
        {
            int i = r.Next(LOW_INT_VAL, HIGH_INT_VAL);

            return i;
        }

        
        /// <param name="minValue">min value random</param>
        /// <param name="maxValue">max value random</param>
        
        public int RandomInt(int minValue, int maxValue)
        {
            int i = r.Next(minValue, maxValue);

            return i;
        }

        
        /// <param name="maxvalue">value for integer</param>
        /// <returns>random integer</returns>
        public int RandomInt(int maxvalue)
        {
            int i = r.Next(maxvalue);

            return i;
        }
    }
}