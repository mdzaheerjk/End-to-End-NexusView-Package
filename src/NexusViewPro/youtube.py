from IPython.display import HTML, display
import re
from NexusViewPro.custom_exception import InvalidURLException
from NexusViewPro.logger import logger

def render_youtube_video(url: str, width: int = 780, height: int = 440):
  try:
    regex = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(regex,url)

    if not match:
      raise InvalidURLException(f"Invalid YouTube URL: {url}")

    video_id = match.group(1)
    embed_url = f"https://www.youtube-nocookie.com/embed/{video_id}"

    iframe = f"""
        <iframe width="{width}" height="{height}" 
        src="{embed_url}" 
        title="YouTube video player" 
        frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
        referrerpolicy="strict-origin-when-cross-origin" 
        allowfullscreen>
        </iframe>
        """

    display(HTML(iframe))
    logger.info(f"Successfully rendered YouTube video for URL: {url}")

    return "success"

  except Exception as e:
    raise e