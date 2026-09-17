import streamlit as st
import sympy as sp
from google import genai

# إعداد صفحة Streamlit
st.set_page_config(page_title="OmniNeural Architecture", layout="centered", page_icon="🧠")

st.title("🧠 OmniNeural Cognitive Architecture")
st.markdown("### Strict Hybrid Deterministic & Linguistic Synthesizer")

# 1. Deterministic Deduction Engine (SymPy Silo)
class DeterministicDeductionEngine:
    def solve_algebraic_equation(self, equation_str: str):
        try:
            x = sp.symbols('x')
            if "=" in equation_str:
                lhs, rhs = equation_str.split("=")
                eq = sp.Eq(sp.sympify(lhs), sp.sympify(rhs))
            else:
                eq = sp.Eq(sp.sympify(equation_str), 0)
            
            solutions = sp.solve(eq, x)
            return {
                "status": "deterministic_solved",
                "engine": "SymPy Symbolic Engine",
                "problem_type": "analytical_problem",
                "target_equation": equation_str,
                "solutions": [str(sol) for sol in solutions]
            }
        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }

# 2. OmniNeural Core (Routing & Silo Management)
class OmniNeuralCore:
    def __init__(self):
        self.deduction_engine = DeterministicDeductionEngine()

    def process_query_silos(self, query: str):
        if "x" in query or "=" in query or "equation" in query.lower():
            eq_part = query.split("equation")[-1].strip() if "equation" in query.lower() else query
            return self.deduction_engine.solve_algebraic_equation(eq_part)
        else:
            return {
                "status": "general_query",
                "result": "No deterministic engine required."
            }

# 3. OmniNeural Synthesizer (Language Cortex with Adaptive Styling)
class OmniNeuralSynthesizer:
    def __init__(self, api_key: str):
        self.client = genai.Client(api_key=api_key)
        self.model_name = 'gemini-3.6-flash'  # الموديل المعتمد للسرعة والدقة
        self.core = OmniNeuralCore()

    def synthesize_answer(self, user_query: str, audience_mode: str = "auto") -> str:
        payload = self.core.process_query_silos(user_query)
        
        if audience_mode == "academic":
            style_instruction = "Use rigorous academic formatting, strict LaTeX notation for all math, and detailed structural breakdowns."
        elif audience_mode == "simple":
            style_instruction = "Use plain, clear language. Do NOT use any LaTeX symbols or dollar signs. Write equations using standard readable text and explain the result directly."
        else:
            style_instruction = "Adapt intelligently: use professional LaTeX notation for mathematical and logical equations, but keep the explanation clear."

        synthesis_prompt = f"""
        You are the Language Cortex (Synthesis Silo) of the OmniNeural cognitive architecture.
        Your strict operational rules:
        1. You are operating as a Closed-System Agent. Do NOT invent or hallucinate any facts, numbers, or calculations.
        2. Your ONLY task is to take the structured System Output Payload provided below and synthesize it into a clear, professional response.
        3. Style Guideline: {style_instruction}
        4. Ensure all mathematical variables, equations, numbers, and symbols match the payload with absolute accuracy.

        System Output Payload:
        {payload}

        Original User Query: "{user_query}"
        """

        response = self.client.models.generate_content(
            model=self.model_name,
            contents=synthesis_prompt,
        )
        return response.text

# --- واجهة المستخدم على الويب (Streamlit Sidebar & Controls) ---
st.sidebar.header("Configuration")
api_key_input = st.sidebar.text_input("Enter Gemini API Key", type="password")

audience_selection = st.sidebar.selectbox(
    "Select Output Mode",
    options=["auto", "academic", "simple"],
    format_func=lambda x: "Auto (Adaptive)" if x == "auto" else ("Academic (LaTeX)" if x == "academic" else "Simple (Plain Text)")
)

user_query = st.text_input("Enter equation or analytical query:", value="x**2 - 4 = 0")

if st.button("Execute OmniNeural Process"):
    if not api_key_input:
        st.error("Please enter your Gemini API Key in the sidebar first!")
    else:
        with st.spinner("Processing through your deterministic core & synthesizing..."):
            try:
                synthesizer = OmniNeuralSynthesizer(api_key=api_key_input)
                result_text = synthesizer.synthesize_answer(user_query, audience_mode=audience_selection)
                
                st.markdown("---")
                st.markdown(result_text)
            except Exception as e:
                st.error(f"An error occurred: {e}")