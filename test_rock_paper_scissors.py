import unittest
from unittest.mock import patch

import rock_paper_scissors as rps


class MockLabel:
    def __init__(self):
        self.text = ''

    def config(self, **kwargs):
        self.text = kwargs.get('text', self.text)


class TestRockPaperScissors(unittest.TestCase):
    def test_determine_winner_tie(self):
        self.assertEqual(rps.determine_winner('rock', 'rock'), "It's a tie!")
        self.assertEqual(rps.determine_winner('paper', 'paper'), "It's a tie!")
        self.assertEqual(rps.determine_winner('scissors', 'scissors'), "It's a tie!")

    def test_determine_winner_player_wins(self):
        self.assertEqual(rps.determine_winner('rock', 'scissors'), 'You win!')
        self.assertEqual(rps.determine_winner('paper', 'rock'), 'You win!')
        self.assertEqual(rps.determine_winner('scissors', 'paper'), 'You win!')

    def test_determine_winner_computer_wins(self):
        self.assertEqual(rps.determine_winner('rock', 'paper'), 'Computer wins!')
        self.assertEqual(rps.determine_winner('paper', 'scissors'), 'Computer wins!')
        self.assertEqual(rps.determine_winner('scissors', 'rock'), 'Computer wins!')

    @patch('rock_paper_scissors.random.choice', return_value='paper')
    def test_get_computer_choice_returns_random_choice(self, mock_choice):
        self.assertEqual(rps.get_computer_choice(), 'paper')
        mock_choice.assert_called_once_with(['rock', 'paper', 'scissors'])

    @patch('rock_paper_scissors.save_high_score')
    @patch('rock_paper_scissors.random.choice', return_value='scissors')
    def test_play_updates_scores_and_labels_for_player_win(self, mock_choice, mock_save):
        result_label = MockLabel()
        score_label = MockLabel()
        high_score_label = MockLabel()

        player_score, computer_score, tie_count, high_score = rps.play(
            'rock', result_label, score_label, high_score_label,
            0, 0, 0, 0
        )

        self.assertEqual(player_score, 1)
        self.assertEqual(computer_score, 0)
        self.assertEqual(tie_count, 0)
        self.assertEqual(high_score, 1)
        self.assertIn('You chose rock. Computer chose scissors.', result_label.text)
        self.assertEqual(score_label.text, 'Score - You: 1, Computer: 0, Ties: 0')
        self.assertEqual(high_score_label.text, 'High Score: 1')
        mock_save.assert_called_once_with(1)

    @patch('rock_paper_scissors.save_high_score')
    @patch('rock_paper_scissors.random.choice', return_value='paper')
    def test_play_updates_scores_for_computer_win(self, mock_choice, mock_save):
        result_label = MockLabel()
        score_label = MockLabel()
        high_score_label = MockLabel()

        player_score, computer_score, tie_count, high_score = rps.play(
            'rock', result_label, score_label, high_score_label,
            0, 0, 0, 0
        )

        self.assertEqual(player_score, 0)
        self.assertEqual(computer_score, 1)
        self.assertEqual(tie_count, 0)
        self.assertEqual(high_score, 0)
        self.assertEqual(score_label.text, 'Score - You: 0, Computer: 1, Ties: 0')
        self.assertEqual(high_score_label.text, 'High Score: 0')
        mock_save.assert_not_called()

    @patch('rock_paper_scissors.save_high_score')
    @patch('rock_paper_scissors.random.choice', return_value='rock')
    def test_play_updates_tie_count_for_tie(self, mock_choice, mock_save):
        result_label = MockLabel()
        score_label = MockLabel()
        high_score_label = MockLabel()

        player_score, computer_score, tie_count, high_score = rps.play(
            'rock', result_label, score_label, high_score_label,
            0, 0, 0, 0
        )

        self.assertEqual(player_score, 0)
        self.assertEqual(computer_score, 0)
        self.assertEqual(tie_count, 1)
        self.assertEqual(high_score, 0)
        self.assertEqual(score_label.text, 'Score - You: 0, Computer: 0, Ties: 1')
        self.assertEqual(high_score_label.text, 'High Score: 0')
        mock_save.assert_not_called()


if __name__ == '__main__':
    unittest.main()
