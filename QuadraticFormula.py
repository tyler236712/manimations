from manim import *

class QuadraticFormula(Scene):
    def construct(self):

        states = [
            "ax^2+bx+c=0",
            "\\frac{ax^2+bx+c=0}{a}",
             "x^2+\\frac{bx}{a}+\\frac{c}{a}=0",
             "x^2+\\frac{bx}{a}=-\\frac{c}{a}",
             "(x+\\frac{b}{2a})^2=-\\frac{c}{a}+\\frac{b^2}{4a^2}",
             "\\sqrt{(x+\\frac{b}{2a})^2}=\\pm\\sqrt{-\\frac{c}{a}+\\frac{b^2}{4a^2}}",
             "x+\\frac{b}{2a}=\\pm\\sqrt{-\\frac{c}{a}+\\frac{b^2}{4a^2}}",
             "x+\\frac{b}{2a}=\\pm\\sqrt{-\\frac{4ac}{4a^2}+\\frac{b^2}{4a^2}}",
             "x+\\frac{b}{2a}=\\pm\\sqrt{\\frac{b^2-4ac}{4a^2}}",
             "x=\\frac{-b}{2a}\\pm\\sqrt{\\frac{b^2-4ac}{4a^2}}",
             "x=\\frac{-b}{2a}\\pm\\frac{\\sqrt{b^2-4ac}}{\\sqrt{4a^2}}",
             "x=\\frac{-b}{2a}\\pm\\frac{\\sqrt{b^2-4ac}}{2a}",
             "x=\\frac{-b\\pm{\\sqrt{b^2-4ac}}}{2a}",
        ]


        curr = MathTex(states[0])
        self.play(Write(curr))
        self.wait()
        
        for i in range(1, len(states)):
            next = MathTex(states[i])
            self.play(ReplacementTransform(curr, next))
            curr = next
            self.wait()

