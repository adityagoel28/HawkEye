import os

from dotenv import load_dotenv
from . import utils

load_dotenv()

header = {
    'authorization': os.environ.get('AAI_API_KEY'),
    'content-type': 'application/json'
}


def transcribe(filename: str, save=False):
    # Upload the audio file to AssemblyAI
    upload_url = utils.upload_file(filename, header)

    # Request a transcription
    transcript_response = utils.request_transcript(upload_url, header)

    # Create a polling endpoint that will let us check when the transcription is complete
    polling_endpoint = utils.make_polling_endpoint(transcript_response)

    # Wait until the transcription is complete
    utils.wait_for_completion(polling_endpoint, header)

    # Request the paragraphs of the transcript
    paragraphs = utils.get_paragraphs(polling_endpoint, header)

    if save:
        # Save and transcript locally
        filename = os.path.splitext(filename)[0]
        with open(f'{filename}_transcript.txt', 'w') as f:
            for para in paragraphs:
                print(para['text'] + '\n')
                f.write(para['text'] + '\n')

    return paragraphs
