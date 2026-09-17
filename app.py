import streamlit as st
import sympy as sp
from google import genai

# إعداد الصفحة لتظهر باحترافية
st.set_page_config(page_title="OmniNeural Architecture", layout="centered")

st.title("🧠 OmniNeural Cognitive Architecture")
st.markdown("### Hybrid Deterministic & Language Synthesis Engine")

# 1. Deterministic Deduction Engine
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
            return {"status": "error", "message": str(e)}

# 2. OmniNeural Core
class OmniNeuralCore:
    def __init__(self):
        self.deduction_engine = DeterministicDeductionEngine()

    def process_query_silos(self, query: str):
        if "x**2" in query or "equation" in query.lower() or "=" in query:
            return self.deduction_engine.solve_algebraic_equation(query)
        else:
            return {"status": "general_query", "result": "No deterministic engine required."}

# 3. OmniNeural Synthesizer
class OmniNeuralSynthesizer:
    def __init__(self, api_key: str):
        self.client = genai.Client(api_key=api_key)
        self.model_name = 'gemini-3.6-flash'
        self.core = OmniNeuralCore()

    def synthesize_answer(self, user_query: str, audience_mode: str = "academic") -> str:
        payload = self.core.process_query_silos(user_query)
        
        if audience_mode == "academic":
            style_instruction = "Use rigorous academic formatting, strict LaTeX notation for all math ($...$ and $$...$$), and detailed structural breakdowns."
        else:
            style_instruction = "Use plain, clear language. Do NOT use LaTeX symbols or dollar signs ($). Write equations simply and explain directly."

        synthesis_prompt = f"""
        You are the Language Cortex (Synthesis Silo) of the OmniNeural cognitive architecture.
        1. Closed-System Agent: Do NOT invent or hallucinate facts or calculations.
        2. Synthesize the provided payload into a professional response.
        3. Style Guideline: {style_instruction}

        System Output Payload:
        {payload}

        Original User Query: "{user_query}"
        """
        response = self.client.models.generate_content(model=self.model_name, contents=synthesis_prompt)
        return response.text

# --- واجهة المستخدم (Streamlit UI) ---
st.sidebar.header("Configuration")
api_key_input = st.sidebar.text_input("Enter Gemini API Key", type="password")
mode = st.sidebar.selectbox("Select Audience Mode", ["academic", "simple"])

user_query = st.text_input("Enter your equation or query:", value="x**2 - 4 = 0")

if st.button("Execute OmniNeural Process"):
    if not api_key_input:
        st.error("Please enter your Gemini API Key in the sidebar first!")
    else:
        with st.spinner("Processing through deterministic & language silos..."):
            try:
                synthesizer = OmniNeuralSynthesizer(api_key=api_key_input)
                result = synthesizer.synthesize_answer(user_query, audience_mode=mode)
                
                st.markdown("---")
                st.markdown(result)
            except Exception as e:
                st.error(f"An error occurred: {e}")