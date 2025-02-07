from pydantic import BaseModel
from crewai.flow.flow import Flow, listen, start
import os
from pathlib import Path
import pandas as pd
from data_processing_tool import DataProcessingTool 
from crews.report_generation_crew.report_generation_crew import ReportGenerationCrew


class SurveyAnalyzerState(BaseModel):
    sample_survey_data: str = ""
    full_survey_data: str = ""
    processed_survey_results: str = ""
    final_report_results: str = ""


class SurveyAnalyzerFlow(Flow[SurveyAnalyzerState]):

    @start()
    def load_survey_data(self):
        """
        Reads a CSV file, converts it into JSON format, and stores it in the Pydantic model.
        """
        print(f"Current working directory: {os.getcwd()}")
        file_path = "src/survey_analysis/data/Crypto_Survey_Data.csv"  # Hardcoded path

    
        # Ensure the file exists
        path = Path(file_path)
        if not path.is_file():
            raise FileNotFoundError(f"File not found: {file_path}")

        # Read CSV into a DataFrame
        df = pd.read_csv(file_path)

        # Convert DataFrame to JSON string
        data_json_str = df.to_json(orient="records")

        # Convert only the first 20 records to JSON
        sample_data = df.head(20).to_json(orient="records")

        # Store the trimmed JSON string in the Pydantic object
        self.state.sample_survey_data = sample_data

        # Store JSON string in the Pydantic object
        self.state.full_survey_data = data_json_str

        print("Survey data successfully loaded into state.")


    @listen(load_survey_data)
    def process_survey_data(self):
        print("Processing survey data...")

        # Instantiate the tool
        tool = DataProcessingTool()

        # Run the tool with the loaded survey data
        result = tool._run(self.state.full_survey_data)

        # Store the processed output in the state variable
        self.state.processed_survey_results = result

        print("Survey data successfully processed.")
        return result

    @listen(process_survey_data)
    def generate_report(self):
        print("Generating report...")
        result = (
            ReportGenerationCrew()
            .crew()
            .kickoff(
                inputs={
                    "processed_survey_results": self.state.processed_survey_results
                }
            )
        )
        self.state.final_report_results = result.raw
        return self.state.final_report_results 


def kickoff():
    survey_flow = SurveyAnalyzerFlow()
    survey_flow.kickoff()


def plot():
    survey_flow = SurveyAnalyzerFlow()
    survey_flow.plot()


if __name__ == "__main__":
    kickoff()
