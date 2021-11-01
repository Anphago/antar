{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Ko_nlp_cleaning.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyNgSp4BvhmhKL1jFVMwubI9",
      "include_colab_link": true
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
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Anphago/antar/blob/main/Ko_nlp_cleaning.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "HqGArv4EZ6FR"
      },
      "source": [
        "# kss install\n",
        "!pip install kss\n",
        "# py hanspell install\n",
        "!pip install git+https://github.com/ssut/py-hanspell.git\n",
        "# PyKoSpacing install\n",
        "!pip install git+https://github.com/haven-jeon/PyKoSpacing.git"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "FCGXQW23Ui11"
      },
      "source": [
        "import re\n",
        "import kss\n",
        "from pykospacing import Spacing\n",
        "from hanspell import spell_checker\n",
        "\n",
        "\n",
        "class Kocleaning():\n",
        "  def __init__(self):\n",
        "    None\n",
        "  \n",
        "  def textcleaning(self, sentence):\n",
        "    cleaned_text = list()\n",
        "    for line in sentence:\n",
        "      for rdata in line:\n",
        "          #raw_text = re.sub(r'[@%\\\\*=()/~#&\\+á?\\xc3\\xa1\\-\\|\\.\\:\\;\\!\\-\\,\\_\\~\\$\\'\\\"]', '', rdata) #remove punctuation\n",
        "          raw_text = re.sub(r'\\d+','', rdata)# remove number\n",
        "          raw_text = re.sub(r'\\s+', ' ', raw_text) #remove extra space\n",
        "          raw_text = re.sub(r'<[^>]+>','',raw_text) #remove Html tags\n",
        "          raw_text = re.sub(r'\\s+', ' ', raw_text) #remove spaces\n",
        "          raw_text = re.sub(r\"^\\s+\", '', raw_text) #remove space from start\n",
        "          raw_text = re.sub(r'\\s+$', '', raw_text) #remove space from the end\n",
        "          raw_text = re.sub(r'[^가-힣\\s]','', raw_text) #remove english spell\n",
        "          raw_text = re.sub(r'[ㅠ]{2,}', '', raw_text)\n",
        "          raw_text = re.sub(r'[ㅋ]{2,}', '', raw_text)\n",
        "          raw_text = re.sub(r'[ㅎ]{2,}', '', raw_text)\n",
        "          cleaned_text.append(raw_text.split('\\t'))\n",
        "    return cleaned_text\n",
        "\n",
        "  def sentence_tokenized(self, sentence):\n",
        "    sentenceToken = list()\n",
        "    for line in sentence:\n",
        "      for rdata in line:\n",
        "        sentenceToken.append(kss.split_sentences(rdata))\n",
        "    return sentenceToken\n",
        "  \n",
        "  def sentence_spacing(self, sentence):\n",
        "    spacing = Spacing()\n",
        "    sentenceSpacing = [[spacing(rdata) for rdata in line]\n",
        "                       for line in sentence]\n",
        "    return sentenceSpacing\n",
        "  \n",
        "  def sentence_spellcheck(self, sentence):    \n",
        "    checked_sent = [[spell_checker.check(rdata) for rdata in line]\n",
        "                for line in sentence]\n",
        "\n",
        "    hanspell_sent = [[rdata.checked for rdata in line]\n",
        "                    for line in checked_sent]\n",
        "    return hanspell_sent"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-96g2TCXXAUS",
        "outputId": "2cb32c52-a693-47c4-91c3-69b5881ec783"
      },
      "source": [
        "sentence = [['애플리케이션 충돌이 맨날 납니다! 개선해 주세요ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ'], ['업데이트 후 gps 위치를 너무 못 잡아요 sm-g970n ㅠㅠㅠㅠㅠㅠㅠㅠ'], [\"왜 새벽에 못 키는 거죠.. What's new에서 서비스 시간을 확인하라는 데 애플리케이션이 열리지도 않는 데 어떻게 확인하라는 건지.. 진짜 애플리케이션 기획 자체가 잘못됨.. 투자 좀 하세요..\"], ['동시 접속자가 많아서 아무것도 할 수 없어요 기다려도 계속 오류 나고. 업데이트가 맞긴 하나요?'], ['계속 동시접속 많다고 뜨네요. 카드라도 보여야 결제를 할 텐데 애플리케이션 왜 이따위로 만들었을 까나'], ['업데이트 이후 사용자편의성은 물론이고 속도도 너무 느려 짐 ..']]\n",
        "\n",
        "ct = Kocleaning()\n",
        "\n",
        "getd = ct.textcleaning(sentence)\n",
        "st = ct.sentence_tokenized(getd)\n",
        "ss = ct.sentence_spacing(st)\n",
        "sc = ct.sentence_spellcheck(ss)\n",
        "\n",
        "print(st)\n",
        "print(ss)\n",
        "print(sc)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[['애플리케이션 충돌이 맨날 납니다 개선해 주세요'], ['업데이트 후 위치를 너무 못 잡아요'], ['왜 새벽에 못 키는 거죠', '에서 서비스 시간을 확인하라는 데 애플리케이션이 열리지도 않는 데 어떻게 확인하라는 건지 진짜 애플리케이션 기획 자체가 잘못됨', '투자 좀 하세요'], ['동시 접속자가 많아서 아무것도 할 수 없어요', '기다려도 계속 오류 나고 업데이트가 맞긴 하나요'], ['계속 동시접속 많다고 뜨네요 카드라도 보여야 결제를 할 텐데 애플리케이션 왜 이따위로 만들었을 까나'], ['업데이트 이후 사용자편의성은 물론이고 속도도 너무 느려 짐']]\n",
            "[['애플리케이션 충돌이 맨날 납니다 개선해 주세요'], ['업데이트 후 위치를 너무 못 잡아요'], ['왜 새벽에 못 키는 거죠', '에서 서비스 시간을 확인하라는 데 애플리케이션이 열리지도 않는 데 어떻게 확인하라는 건지 진짜 애플리케이션 기획 자체가 잘못됨', '투자 좀 하세요'], ['동시 접속자가 많아서 아무것도 할 수 없어요', '기다려도 계속 오류 나 고 업데이트가 맞긴 하나요'], ['계속 동시접속 많다고 뜨네요 카드라도 보여야 결제를 할 텐데 애플리케이션 왜 이 따위로 만들었을 까나'], ['업데이트 이후 사용자 편의성은 물론이고 속도도 너무 느려 짐']]\n",
            "[['애플리케이션 충돌이 맨날 납니다 개선해 주세요'], ['업데이트 후 위치를 너무 못 잡아요'], ['왜 새벽에 못 키는 거죠', '에서 서비스 시간을 확인하라는 데 애플리케이션이 열리지도 않는 데 어떻게 확인하라는 건지 진짜 애플리케이션 기획 자체가 잘못됨', '투자 좀 하세요'], ['동시 접속자가 많아서 아무것도 할 수 없어요', '기다려도 계속 오류 나 고 업데이트가 맞긴 하나요'], ['계속 동시 접속 많다고 뜨네요 카드라도 보여야 결제를 할 텐데 애플리케이션 왜 이따위로 만들었을 까나'], ['업데이트 이후 사용자 편의성은 물론이고 속도도 너무 느려짐']]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "JFx0ILMVgenP"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}