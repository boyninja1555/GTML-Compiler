"use strict";
// import * as vscode from 'vscode';
Object.defineProperty(exports, "__esModule", { value: true });
exports.deactivate = exports.activate = void 0;
// export function activate(context: vscode.ExtensionContext) {
//   context.subscriptions.push(
//     vscode.languages.registerDocumentFormattingEditProvider('gtml', {
//       provideDocumentFormattingEdits(document: vscode.TextDocument): vscode.TextEdit[] {
//         const textEdits: vscode.TextEdit[] = [];
//         const text = document.getText();
//         // Simple formatter to indent contents of GTML tags
//         const formattedText = text.replace(
//           /(\{[^}]+\})([^]*?)(\{END:[^}]+\})/g,
//           (match: string, p1: string, p2: string, p3: string) => {
//             const indent = '    ';
//             const indentedContent = p2.split('\n').map((line: string) => line.trim() ? indent + line.trim() : '').join('\n');
//             return `${p1}\n${indentedContent}\n${p3}`;
//           }
//         );
//         const entireRange = new vscode.Range(
//           document.positionAt(0),
//           document.positionAt(text.length)
//         );
//         textEdits.push(vscode.TextEdit.replace(entireRange, formattedText));
//         return textEdits;
//       }
//     })
//   );
// }
// export function deactivate() {}
const vscode = require("vscode");
function activate(context) {
    context.subscriptions.push(vscode.languages.registerDocumentFormattingEditProvider('gtml', {
        provideDocumentFormattingEdits(document) {
            const textEdits = [];
            const text = document.getText();
            // Simple formatter to indent contents of GTML tags
            const formattedText = text.replace(/(\{[^}]+\})([^]*?)(\{END:[^}]+\})/g, (match, p1, p2, p3) => {
                const indent = '    ';
                const indentedContent = p2.split('\n').map((line) => line.trim() ? indent + line.trim() : '').join('\n');
                return `${p1}\n${indentedContent}\n${p3}`;
            });
            const entireRange = new vscode.Range(document.positionAt(0), document.positionAt(text.length));
            textEdits.push(vscode.TextEdit.replace(entireRange, formattedText));
            return textEdits;
        }
    }));
}
exports.activate = activate;
function deactivate() { }
exports.deactivate = deactivate;
//# sourceMappingURL=extension.js.map