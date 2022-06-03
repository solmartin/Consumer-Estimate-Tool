#!/usr/bin/env python3

"""A simple python script template.

"""

import os
import sys
import argparse
import re


class ConsumerDetails():

    def __init__(self, inputs):
        # Parse input list extracted from consumer interface
        # Add instance variables for each criteria
        self.input = re.findall(r'\[.*?\]', inputs)
        
        self.landscape = {}
        self.junk = {}
        self.move = {}
        self.inPaint = {}
        self.exPaint = {}

        self.parseMove()
        # self.parseInPaint()
        # self.parseExPaint()

        self.move['total'] = generateMovingEstimate(self)
        print(self.move['total'])
        # raise NotImplementedError

    def parseMove(self): # Organize moving data
        # example self.input[2] after being split by previous parse:
        # [4, 1, 0, 2, 70.5, 344.72, 4]
        print(self.input[2])
        # self.input[2] = re.split(r'\[|\,|\]', self.input[2])
        # self.input[2] = re.split(r'(\W+?)', self.input[2])
        self.input[2] = re.findall(r'\d+\.*\d*', self.input[2])
        print(self.input[2])
        self.move['numRooms'] = int(self.input[2][0])
        self.move['packing'] = int(self.input[2][1])
        self.move['assemble'] = int(self.input[2][2])
        self.move['numFlights'] = int(self.input[2][3])
        self.move['mileage'] = float(self.input[2][4])
        self.move['gas'] = float(self.input[2][5])
        self.move['travelTime'] = float(self.input[2][6]) 

    def parseInPaint(self):

        self.inPaint['numRooms'] = int()
        self.inPaint['sqftWall'] = float()
        self.inPaint['sqftCeil'] = float()
        self.inPaint['numDoors'] = int()
        self.inPaint['trimLength'] = float() # In feet. This may be an incorrect interpretation
        self.inPaint['numWindows'] = int()
        self.inPaint['numWindowCasing'] = int()
        self.inPaint['cleanUp'] = int() # boolean
        self.inPaint['numClosets'] = int()

        raise NotImplementedError

    def parseExPaint(self):
        raise NotImplementedError

def generateMovingEstimate(consumer):
    input = consumer.move
    
    if input['numRooms'] == 0:
        locals = 2
        jobHrs = 2
        uhaul = 83
    elif input['numRooms'] == 1:
        locals = 2
        jobHrs = 3
        uhaul = 94
    elif input['numRooms'] == 2:
        locals = 2
        jobHrs = 4
        uhaul = 94
    elif input['numRooms'] == 3:
        locals = 3
        jobHrs = 6
        uhaul = 103
    elif input['numRooms'] == 4:
        locals = 4
        jobHrs = 7
        uhaul = 103
    else: raise ValueError("Number of bedrooms cannot be greater than 4")

    packVar = 2 if input['packing'] else 0
    assembleVar = 0.25 if input['assemble'] else 0
    flightVar = (input['numFlights'] - 1)*0.05 + 0.1 if input['numFlights'] > 0 else 0 # Maybe throw an error if numFlights > 5?
    extras = packVar + assembleVar + flightVar

    driving = uhaul + input['mileage'] + input['gas'] # TODO: abstract mileage and gas from the user, just use location/gas prices
    labor = 45*locals
    totalHrs = jobHrs + input['travelTime'] # TODO: abstract travel time via google maps
    laborTotal = labor*(totalHrs + extras)

    print(f'\nLabor is {labor}.\nTotal time is {totalHrs} hours.\nLabor total is ${laborTotal}.\nDriving total is ${driving}.')
    return laborTotal + driving

def generateInPaintingEstimate(consumer):
    input = consumer.inPaint

    jobTime = input['numRooms'] + 2*input['sqftWall']/100 + 2.5*input['sqftCeil']/100 + input['numDoors'] + \
        input['trimLength']/24 + input['numWindows'] + 0.25*input['numWindowCasing'] + 1.25*input['cleanUp'] + \
        4*input['numClosets']

    # TODO: Include Material Cost
    # TODO: Update estimate based on fine details (as seen in document)

    total = 0 # TODO: Fill in proper subtotal
    estimate = [0.85*total, 100 + 1.15*total]
    raise NotImplementedError
    



def main():
    ConsumerDetails('[], [], [4, 1, 0, 2, 70.5, 344.72, 4], []')

if __name__ == '__main__':
    main()