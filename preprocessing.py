{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "preprocessing.py",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyP1fMGRCgotoBVX+LZdNSWT"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "metadata": {
        "id": "dDUbrNOMwJ8e"
      },
      "source": [
        "import re\n",
        "import nltk\n",
        "from nltk.tokenize import word_tokenize\n",
        "from nltk.stem import WordNetLemmatizer\n",
        "#from kss import split_sentences\n",
        "\n",
        "\n",
        "class Tcleaning:\n",
        "  pass\n",
        "\n",
        "\n",
        "#  def __init__(self, rdata):\n",
        "#    pass\n",
        "  \n",
        "\"\"\"\n",
        "  def language_detection(self, rdata):\n",
        "    len_ko = len(re.sub(\"[^가-힇]\", \"\", self.rdata))\n",
        "    len_en = len(re.sub(\"[^a-zA-Z]\", \"\", self.rdata))\n",
        "    return \"ko\" if len_ko >= len_en else \"en\"\n",
        "\"\"\"\n",
        "\n",
        "\n",
        "#class Morpheme():\n",
        "#  def __init__(self):"
      ],
      "execution_count": 5,
      "outputs": []
    }
  ]
}